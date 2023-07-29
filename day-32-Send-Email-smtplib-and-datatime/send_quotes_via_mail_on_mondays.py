import datetime as dt
import smtplib
import random

my_email = "raj.aryan.788010@gmail.com"
my_app_password = 'izbyhaamyevvkrrb'

if dt.datetime.now().weekday() == 5:
    with open("quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  # tls -> Transport Layer Security
        connection.login(user=my_email, password=my_app_password)
        connection.sendmail(from_addr=my_email, to_addrs='jackdenial62@gmail.com',
                            msg=f"Subject:Daily Saturday Motivation\n\n{quote}")

