import requests

ISS_URL = "http://api.open-notify.org/iss-now.json"
response = requests.get(url=ISS_URL)
response.raise_for_status()

data = response.json()["iss_position"]
latitude = data["latitude"]
longitude = data["longitude"]

iss_position = (longitude, latitude)
print(iss_position)
