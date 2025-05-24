import time
from dotenv import load_dotenv
from datetime import datetime

from services.fetch_weather import fetch_weather
from services.txt_file import create_log
from services.excel_file import save_to_excel
from services.mongodb import save_to_mongo
from services.mysql_db import save_to_mysql, get_from_mysql
from config import Config

load_dotenv()

def start():
    weather = fetch_weather(Config.API_KEY, Config.CITY)
    create_log(
        Config.LOG_FILENAME,
        f"{datetime.now()}: Pobrano dane pogodowe miasta: {Config.CITY}\n"
    )
    match Config.OPERATION:
        case 1:
            save_to_excel(Config.EXCEL_FILENAME, weather)
        case 2:
            save_to_mongo(weather)
        case 3:
            save_to_excel(Config.EXCEL_FILENAME, weather)
            save_to_mongo(weather)
        case 4:
            save_to_mysql(weather)
        case _:
            print("Nie rozpoznano operacji!")

def show_last_10_operations():
    try:
        with open(Config.LOG_FILENAME, 'r') as file:
            lines = file.readlines()
        last_10 = lines[-10:]
        print("Ostatnie 10 operacji:")
        for line in last_10:
            print(line.strip())
    except FileNotFoundError:
        print("Brak pliku logu. Nie wykonano jeszcze żadnych operacji.")

def main():
    print("Co chcesz zrobić?")
    print("a) Pobierz dane pogodowe miasta")
    print("b) Wyświetl ostatnie 10 operacji")
    choice = input("Wybierz opcję (a/b): ").strip().lower()

    if choice == 'a':
        Config.CITY = input("Podaj nazwę miasta: ")
        print("Co chcesz zrobić z danymi?")
        print("1. Zapisz do pliku Excel")
        print("2. Zapisz do MongoDB")
        print("3. Zapisz do pliku Excel i do MongoDB")
        print("4. Zapisz do MySQL")
        try:
            Config.OPERATION = int(input("Wybierz rodzaj operacji (1-4): "))
        except ValueError:
            print("Nieprawidłowy wybór operacji.")
            return

        while True:
            try:
                start()
                print("Pobrano dane")
            except Exception as e:
                print(e)
                create_log(
                    Config.LOG_FILENAME,
                    f"{datetime.now()}: Wystąpił błąd {e} podczas pobierania danych dla miasta: {Config.CITY}\n"
                )
            time.sleep(10)

    elif choice == 'b':
        show_last_10_operations()

    else:
        print("Nieprawidłowy wybór. Wybierz 'a' lub 'b'.")

if __name__ == "__main__":
    main()
