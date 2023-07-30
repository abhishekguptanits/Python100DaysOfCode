import requests

KANYE_QUOTES_API = 'https://api.kanye.rest'

try:
    response = requests.get(url=KANYE_QUOTES_API)
    response.raise_for_status()
    data = response.json()
    quote = data['quote']
except Exception as err:
    print(str(err))
else:
    print(quote)