import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "raj.aryan.788010@gmail.com"
MY_APP_PASSWORD = 'izbyhaamyevvkrrb'

RECIPIENT_EMAIL = 'jackdenial62@gmail.com'

MY_LAT = 25.292106
MY_LONG = 83.657762


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


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

    time_now = datetime.now().hour

    if time_now >= sunset+3 or time_now <= sunrise-2:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()  # tls -> Transport Layer Security
            connection.login(user=MY_EMAIL, password=MY_APP_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=RECIPIENT_EMAIL,
                msg="Subject:Look up for ISS\n\nThe ISS is visible in the sky above, Go have a look!"
            )

