from datetime import datetime
import smtplib
import pandas
import random

MY_EMAIL = "raj.aryan.788010@gmail.com"
MY_APP_PASSWORD = 'izbyhaamyevvkrrb'

today_month = datetime.now().month
today_day = datetime.now().day
today = (today_month, today_day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    letter_file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(letter_file_path) as letter_file:
        letter_content = letter_file.read()
        updated_letter_content = letter_content.replace("[NAME]", birthday_person["greeting-name"])

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_APP_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{updated_letter_content}"
        )





