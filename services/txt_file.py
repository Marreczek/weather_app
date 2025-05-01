from config import Config
from datetime import datetime

def create_log(message: str, filename=Config.LOG_FILENAME):
    with open(filename, "a", encoding="utf-8") as logs:
        logs.write(f"{message}\n")

#funkcja dla odczytywania treści pliku logs.txt
def logs_read():
    with open(Config.LOG_FILENAME,"r", encoding="utf-8") as lines:
        for line in lines:
            print(line.strip())