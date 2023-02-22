# API

# Application Programming Interface


import requests

response = requests.get(url="http://api.open-notify.org/astros.json")

# if response.status_code != 200:
#    raise Exception("Bad exception from ISS API")

# if response.status_code == 404:
#    raise Exception("That resource does not exist")
response.raise_for_status()   # we put all of exceptions here

data = response.json()

print(data)


