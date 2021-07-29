import requests
from datetime import datetime
import config

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# exercise_text = input("What exercise did you do? ")

exercise_body = {
    "query": "ran 5 kilometers",
    "gender": "male",
    "weight_kg": 88,
    "height_cm": 183,
    "age": 33,
}

exercise_header = {
    "x-app-id": config.APP_ID,
    "x-app-key": config.API_KEY,
    # "Content-Type": "json"
}

response_from_exercise = requests.post(exercise_endpoint, json=exercise_body, headers=exercise_header)
response_from_exercise = response_from_exercise.json()
today = datetime.now().strftime("%Y-%m-%d")
today_time = datetime.now().strftime("%X")
exercise_name = response_from_exercise["exercises"][0]["name"]
exercise_calories = response_from_exercise["exercises"][0]["nf_calories"]
exercise_duration = response_from_exercise["exercises"][0]["duration_min"]
print(response_from_exercise)
print(today)
print(exercise_name)
print(exercise_calories)

excel_endpoint = "https://api.sheety.co/a16a777eeb0f532c8eda0e87a6dd72b4/myWorkouts/workouts"
excel_body = {
    "workout": {
        "date": today,
        "time": today_time,
        "exercise": exercise_name.title(),
        "duration": exercise_duration,
        "calories": exercise_calories,
    }
}

bearer_headers = {
    "Authorization": f"Bearer {config.SHEETY_TOKEN}"
}

response_from_excel = requests.post(excel_endpoint, json=excel_body, headers=bearer_headers)
