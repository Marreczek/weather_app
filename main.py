from os import environ
from dotenv import load_dotenv
from services.fetch_weather import fetch_weather
load_dotenv()
from services.txt_file import create_log
from datetime import datetime

API_KEY = environ.get("API_KEY")
CITY = environ.get("CITY")

try:
    weather = fetch_weather(API_KEY,CITY)
    create_log(f"{datetime.now()}: Pobrano dane pogodowe miasta: {CITY}\n")
    print(weather)
except Exception as e:
    print(e)
    create_log(f"{datetime.now()}: Wystapił błąd {e} podczas pobierania danych dla miasta: {CITY}\n")