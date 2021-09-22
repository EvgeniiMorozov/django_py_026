import requests


WEATHER_API_URL = "https://api.openweathermap.org/data/2.5"
WEATHER_API_KEY = "2067eeaf5536086acde12a04f8037f47"


def one_call_weather(latitude, longitude):
    url = WEATHER_API_URL + "/onecall?"
    payload = {"lat": latitude, "lon": longitude, "units": "metric", "lang": "ru", "appid": WEATHER_API_KEY}
    return requests.get(url, payload).json()


def city_weather_call(city_name):
    url = WEATHER_API_URL + "/weather?"
    payload = {"q": city_name, "units": "metric", "lang": "ru", "appid": WEATHER_API_KEY}
    return requests.get(url, payload).json()
