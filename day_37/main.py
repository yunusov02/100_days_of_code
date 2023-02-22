import requests

pixela_endpoint= "https://pixe.la/v1/users"


user_params = {
    'token': 'afdsfnti3453hhbk34bjh',
    'username': 'Asilbek',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)
