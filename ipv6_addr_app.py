import urllib.parse
import requests
import json

main_api = "https://ipapi.co/"
ip = "200.2.1.53"
format = "/json/"

url = (main_api + format)
print(url)

api_response = requests.get(url).json()

print(api_response)

