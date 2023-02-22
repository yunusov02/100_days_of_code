import requests
import datetime

MY_LAT = 40.874832
MY_LONG = 69.598898
parameters = {
    'lat': MY_LAT,
    'long': MY_LONG,
    'formatted': 0
}


response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data['results']['sunrise']
sunset = data['results']['sunset']

print(sunrise)
time_now = datetime.datetime.now()
print(time_now)




