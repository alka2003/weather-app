import requests, json, os
from datetime import datetime

API_KEY = "YOUR_API_KEY_HERE"
CURRENT_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"
CACHE_FILE = "weather_cache.json"


def kelvin_to_celsius(k):
    return round(k - 273.15, 2)


def load_cache():
    return json.load(open(CACHE_FILE)) if os.path.exists(CACHE_FILE) else {}


def save_cache(cache):
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f)


def get_weather(city):
    cache = load_cache()
    if city in cache:
        return cache[city]

    params = {"q": city, "appid": API_KEY}
    response = requests.get(CURRENT_URL, params=params)
    if response.status_code != 200:
        raise Exception("Error fetching weather")

    data = response.json()
    cache[city] = data
    save_cache(cache)
    return data


def get_forecast(city):
    params = {"q": city, "appid": API_KEY}
    response = requests.get(FORECAST_URL, params=params)
    if response.status_code != 200:
        raise Exception("Error fetching forecast")
    return response.json()
