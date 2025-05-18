from pymongo import MongoClient
from config import Config

def db():
    client = MongoClient(Config.DB_URI)
    db = client["miasta_db"]
    collection = db["weather"]

    return collection

def save_to_mongo(data):
    try:
        mongo = db()
        mongo.insert_one(data)
        print("Zapisano do bazy danych")
    except Exception as e:
        print(e)