import requests
import time
from datetime import datetime

from utils.to_celsius import to_celsius
from utils.km_h import ms_to_kmh


def fetch_weather(token: str,city: str):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}"

    try:
        response  = requests.get(url)
        data = response.json()

        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        weather = {
            "timestamp": timestamp,
            "name": data["name"],
            "temp": to_celsius(data["main"]["temp"]),
            "feels_like": to_celsius(data["main"]["feels_like"]),
            "humidity": data["main"]["humidity"],
            "wind_speed": ms_to_kmh(data["wind"]["speed"])
        }

        return weather

    except Exception as e:
        print(e)