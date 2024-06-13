import requests
api_key = '005b3775f3646b734caa0cf6d9b167b4'
city = 'Karimnagar'
base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
response = requests.get(base_url)
weather_data = response.json()
print(f"Current Weather in {city}:")
print(f"Weather: {weather_data['weather'][0]['description']}")
print(f"Temperature: {weather_data['main']['temp']}°C")
print(f"Humidity: {weather_data['main']['humidity']}%")
print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
forecast_response = requests.get(forecast_url)
forecast_data = forecast_response.json()
print("\n5-Day Temperature Trends:")
for forecast in forecast_data['list']:
    print(f"Date: {forecast['dt_txt']}, Temperature: {forecast['main']['temp']}°C")