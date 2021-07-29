##################### Extra Hard Starting Project ######################
import random
import pandas
from datetime import datetime
import smtplib
import configs

from os import path

# 2. Check if today matches a birthday in the birthdays.csv
today = datetime.now()
today_tuple = (today.month, today.day)

print('__file__', path.dirname(__file__))

data = pandas.read_csv(path.join(path.dirname(__file__), 'birthdays.csv'))
# data = pandas.read_csv(".birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]["name"]
    file_name = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    file_path = (path.join(path.dirname(__file__), file_name))
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person)

    with smtplib.SMTP(configs.SMTP_GMAIL) as connection:
        connection.starttls()
        connection.login(configs.MY_EMAIL, configs.PASSWORD)
        connection.sendmail(from_addr=configs.MY_EMAIL,
                            to_addrs=configs.RECEIVE_EMAIL,
                            msg=f"Subject:Happy Birthday!\n\n{contents}")
