import json
import requests


city_name = 'Moscow'
key = 'd8c23f7eb383775fbb900fc5a500700d'
response = requests.post(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}')
result = json.loads(response.text)

city_name = result.get('name', 'Unknown city')
weather_info = result.get('weather', [{}])[0].get('description', 'No weather data')
humidity = result.get('main', {}).get('humidity', 'No humidity data')
pressure = result.get('main', {}).get('pressure', 'No pressure data')
temperature = result.get('main', {}).get('temp', 'No temp data')


print(f"Город: {city_name}")
print(f"Погода: {weather_info}")
print(f"Влажность: {humidity}%")
print(f"Давление: {pressure} hPa")
print(f"Температура: {temperature} °K  или  ", round(temperature - 273, 2), "°C" )