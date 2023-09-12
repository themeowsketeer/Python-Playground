import json

import requests
from pprint import pprint
import json as js

API = 'e4d8849826c2311791bc18c4339776b3'

# city = input('Enter a city: ')

city = 'hanoi'

url = 'https://api.openweathermap.org/data/2.5/weather?appid=' + API + '&q=' + city

weatherData = requests.get(url).json()

pprint(weatherData['clouds']['all'])