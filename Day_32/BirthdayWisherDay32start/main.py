# import smtplib
# from configs import my_email, password, receive_mail
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs=receive_mail,
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )
# -------------------------------
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.isoweekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1988, month=7, day=1)
# print(date_of_birth)
# -------------------------------
import datetime
import smtplib
import datetime as dt
from configs import MY_EMAIL, RECEIVE_EMAIL, PASSWORD, SMTP_GMAIL
import random

now = datetime.datetime.now()
day = now.strftime("%A")


def chose_quote():
    with open("quotes.txt", "r", encoding='utf-8') as quotes:
        all_quotes = [line for line in quotes.readlines()]
        random_quote = random.choice(all_quotes)
    return random_quote


with smtplib.SMTP(SMTP_GMAIL) as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=RECEIVE_EMAIL,
        msg=f"Subject:Motivation quote\n\n{day}\n{chose_quote()}".encode("utf8"),
    )
