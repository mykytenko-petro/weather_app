import requests
from .write_json import write_json
# requests - модуль для відправки запитів
# get - отримує дані за посиланням
city_name = 'Dnipro'
api_key = "f45b384d06f8d6558d2f50d57cd3220f"

url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&lang=ua&units=metric'

data = requests.get(url)
if data.status_code == 200:
    write_json("weather_data.json", data.json())
else:
    print("Error - ",data.status_code)