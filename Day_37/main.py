import requests
from datetime import datetime

USERNAME = "viktorkrd"
TOKEN = "fdgtdy3afasfwerg124"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# today = datetime(year=2021, month=7, day=18).strftime("%Y%m%d")
today = datetime.now().strftime("%Y%m%d")

pixel_config = {
    "date": today,
    "quantity": input("How many kilometers did you running today? "),
}

response = requests.post(pixel_creation_endpoint, json=pixel_config, headers=headers)
print(response.text)
pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

pixel_update_config = {
    "quantity": "2",
}

# response = requests.put(pixel_update_endpoint, json=pixel_update_config, headers=headers)
# print(response.text)

# response = requests.delete(pixel_update_endpoint, headers=headers)
# print(response.text)
