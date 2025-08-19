"""Rain forecast"""

import os

import requests

LAT = 29.978375599483314
LON = 76.873516602435
API_KEY = os.environ.get("APIKEY")
API = "https://api.openweathermap.org/data/2.5/forecast"

PARAMETERS = {
    "lat": LAT,
    "lon": LON,
    "cnt": 4,
    "appid": API_KEY,
}

try:
    response = requests.get(url=API, params=PARAMETERS, timeout=20)
    response.raise_for_status()
except requests.RequestException as e:
    print(f"Failed to get weather data: {e}")
else:
    weather_data = response.json()
    IS_RAIN = False
    for hour_data in weather_data["list"]:
        weather_code = hour_data["weather"][0]["id"]
        if weather_code < 700:
            IS_RAIN = True

if IS_RAIN:
    print("Bring an umbrella!")
