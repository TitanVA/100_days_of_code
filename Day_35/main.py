import requests
from flask import Flask, jsonify
from twilio.rest import Client

API_KEY = "d100e2f457e38090f85145e050b82cd0"
LAT = 52.07
LON = 38.14
API_REQUEST = "https://api.openweathermap.org/data/2.5/onecall"
ACC_SID = "AC79b6fe7c786a155da067f52b210bdeb7"
ACC_TOKEN = "be3080733f345c2983159ba84f9185a6"



def get_weather():
    parameters = {
        "lat": LAT,
        "lon": LON,
        "appid": API_KEY,
        "exclude": "current,minutely,daily"
    }

    response = requests.get(API_REQUEST, params=parameters)
    response.raise_for_status()
    weather_data = response.json()
    hourly_data = weather_data["hourly"][0:12]

    will_rain = False

    for data in hourly_data:
        condition_code = data["weather"][0]["id"]
        if int(condition_code) < 700:
            will_rain = True
    if will_rain:
        client = Client(ACC_SID, ACC_TOKEN)

        message = client.messages \
            .create(
            body="It's going to rain today 🌨. Remember to bring an umbrella ☂",
            from_="+14159910027",
            to="+79183209852"
        )
    print(message.sid)


get_weather()

# app = Flask(__name__)
#
#
# @app.route('/data/', methods=['GET', 'POST'])
# def welcome():
#     return jsonify(get_weather())
#
#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=4002)
#
# app.run()
