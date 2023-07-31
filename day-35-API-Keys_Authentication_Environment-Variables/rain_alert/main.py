import requests
import time
import env

owm_api_key = env.OWM_API_KEY

MY_LAT = 27.2585
MY_LNG = 75.1799

# weather_params = {
#     'lat': MY_LAT,
#     'lon': MY_LNG,
#     'appid': OWM_API_KEY,
# }

weather_params = {
    'q': 'Amsterdam,Netherlands',
    'appid': owm_api_key,
}

OWM_ENDPOINT = 'https://api.openweathermap.org/data/2.5/weather'

will_rain = False
try:
    response = requests.get(url=OWM_ENDPOINT, params=weather_params)
    response.raise_for_status()
    weather_data = response.json()
    weather_condition = weather_data['weather'][0]
    weather_id = weather_condition['id']
    weather = weather_condition['main']
except Exception as err:
    print(str(err))
else:
    if weather_id < 700:
        will_rain = True
    # time.sleep(3600)    # Checks for the Weather condition each hour

if will_rain:
    print('Today it might rain, so Bring an Umbrella!')




