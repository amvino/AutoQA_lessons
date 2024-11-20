#Узнайте текущий курс евро (EUR) к доллару США (USD).

import requests


url = "https://api.exchangerate-api.com/v4/latest/USD"
# API_KEY = 'mmayUu9KKeqv425UyQE84caUdQuOm04ROgO5JKCbih8'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    euro_rate = data["rates"].get("RUB")
    if euro_rate:
        print(f'Курс {euro_rate}')
else:
    print('fuAPI')