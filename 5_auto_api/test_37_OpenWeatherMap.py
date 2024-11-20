#Отправьте запрос с параметрами q=(калининград) и вашим appid (ключ API). Получите текущую температуру и погодные условия в Калининграде

import requests

url = "https://api.openweathermap.org/data/2.5/weather"
params = {
   "q": "Kaliningrad",
   "appid": "1716b91f56f380231d3e3325e096413e",  # Замените на ваш ключ OpenWeatherMap
   "units": "metric",
   "lang": "ru"
}

response = requests.get(url, params=params)

if response.status_code == 200:
   data = response.json() 
   temperature = data["main"]["temp"]
   weather_description = data["weather"][0]["description"]

   print(f"Температура в Калининграде: {temperature}°C")
   print(f"Погодные условия: {weather_description}")

else:
   print(f"Ошибка при запросе API: {response.status_code}")