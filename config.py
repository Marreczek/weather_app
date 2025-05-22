import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    API_KEY = os.environ.get("API_KEY")
    CITY = os.environ.get("CITY")
    DB_URI = os.environ.get("DB_URI")
    LOG_FILENAME = "logs.txt"
    EXCEL_FILENAME = "pogoda.xlsx"

    MYSQL_USER = os.environ.get("MYSQL_USER")
    MYSQL_PASS = os.environ.get("MYSQL_PASS")
    MYSQL_HOST = os.environ.get("MYSQL_HOST")
    MYSQL_DB = os.environ.get("MYSQL_DB")