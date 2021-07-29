import time
import smtplib
import requests
from datetime import datetime
from configs import MY_EMAIL, RECEIVE_EMAIL, PASSWORD, SMTP_GMAIL

MY_LAT = 45.039268  # Your latitude
MY_LONG = 38.987221  # Your longitude


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    return sunset < time_now.hour < sunrise


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return abs(iss_latitude - MY_LAT) < 5 and abs(iss_longitude - MY_LONG) < 5


while True:
    if is_iss_overhead() and is_night():
        # Then send me an email to tell me to look up.
        with smtplib(SMTP_GMAIL) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=RECEIVE_EMAIL,
                msg=f"Subject:ISS under You ☝\n\nThe ISS is above you in the sky",
            )
    # BONUS: run the code every 60 seconds.
    print("Wait 60 sec")
    time.sleep(60)
