import requests
from datetime import datetime

SOLAR_SCHEDULE_ENDPOINT = 'https://api.sunrise-sunset.org/json'
ISS_ENDPOINT = 'http://api.open-notify.org/iss-now.json'

try:
    response = requests.get(url=ISS_ENDPOINT)
    response.raise_for_status()
    data = response.json()
    latitude = data['iss_position']['latitude']
    longitude = data['iss_position']['longitude']
except Exception as err:
    print(str(err))


co_ordinates = {
    'lat': latitude,
    'lng': longitude,
    'formatted': 0
}

try:
    response = requests.get(url=SOLAR_SCHEDULE_ENDPOINT, params=co_ordinates)
    response.raise_for_status()
    data = response.json()
    sunrise = data['results']['sunrise']
    sunrise_time = sunrise.split('T')[1]
    sunrise_hour = sunrise_time.split(':')[0]

    sunset = data['results']['sunset']
    sunset_time = sunset.split('T')[1]
    sunset_hour = sunset_time.split(':')[0]
except Exception as err:
    print(str(err))
else:
    print(sunrise_hour)


current_time = datetime.now().time()
current_hour = current_time.hour
print(current_hour)