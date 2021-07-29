import requests
from datetime import datetime

MY_LAT = 45.039268
MY_LNG = 38.987221

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

SUNSET_API = "https://api.sunrise-sunset.org/json"
response = requests.get(SUNSET_API, params=parameters)
response.raise_for_status()
data = response.json()["results"]
sunrise = data["sunrise"].split("T")[1].split(":")[0]
sunset = data["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)