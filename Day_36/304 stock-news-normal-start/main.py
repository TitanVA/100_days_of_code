import datetime
from twilio.rest import Client
import requests
import pandas
import csv
import config

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# today_data = datetime.date.today()
# yesterday_data = today_date - datetime.timedelta(days=3)
# yesterday_data = yesterday_date.strftime("%Y-%m-%d")
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": config.API_PRICE,
}
response = requests.get(STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
tesla_data = response.json()['Time Series (Daily)']
tesla_data_list = [value for (key, value) in tesla_data.items()]
yesterday_data = tesla_data_list[0]
yesterday_closing_price = float(yesterday_data['4. close'])
before_yesterday_data = tesla_data_list[1]
before_yesterday_closing_price = float(before_yesterday_data['4. close'])
print(f"Close prise yesterday: {yesterday_closing_price}")
print(f"Close prise before yesterday: {before_yesterday_closing_price}")
difference = yesterday_closing_price - before_yesterday_closing_price
percent = (before_yesterday_closing_price - yesterday_closing_price) / yesterday_closing_price * 100
if difference > 0:
    print(f"Upper 💹 by {round(percent, 2)} percent")
    if percent > 5:
        print("Get News")
elif difference < 0:
    print(f"Down 🔻 by {round(percent, 2)} percent")
else:
    print("Same price")


new_parameters = {
    "q": COMPANY_NAME,
    "apiKey": config.API_NEWS,
}
response = requests.get(NEWS_ENDPOINT, params=new_parameters)
response.raise_for_status()
news_data = response.json()['articles'][:3]
formated_articles = [f"Headline: {new['title']}. \nBrief: {new['description']}" for new in news_data]
print(formated_articles)


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.
# Send each article as a separate message via Twilio.
client = Client(config.TWILIO_SID, config.TWILIO_TOKEN)
for article in formated_articles:
    message = client.messages.create(
        body=article,
        from_="+14159910027",
        to="+79183209852",
    )

    # Optional Format the message like this:
    """
    TSLA: 🔺2%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    or
    "TSLA: 🔻5%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    """
