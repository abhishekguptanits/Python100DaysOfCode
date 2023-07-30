import requests

ISS_ENDPOINT = 'http://api.open-notify.org/iss-now.json'

response = requests.get(url=ISS_ENDPOINT)

# try:
#     if response.status_code == 200:
#         print(response.json())
#     elif response.status_code == 404:
#         raise Exception("Resource does not exist.")
#     elif response.status_code == 401:
#         raise Exception("You are not authorized.")
#     else:
#         raise Exception(f"Error {response.status_code}")
# except Exception as err:
#     print(f"Error: {str(err)}")

try:
    response.raise_for_status()
    data = response.json()
    iss_position = data['iss_position']
    latitude = data['iss_position']['latitude']
    longitude = data['iss_position']['longitude']
    print(f'Response: {data}')
    print(f'ISS Position {iss_position}')
    print(f'Latitude: {latitude}')
    print(f'Longitude: {longitude}')
except Exception as err:
    print(str(err))

