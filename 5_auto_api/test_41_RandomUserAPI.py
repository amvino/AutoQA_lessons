#Сделайте запрос для генерации 5 случайных пользователей (параметр results=5). Выведите их имена и адреса электронной почты.

import requests


url = "https://randomuser.me/api"
# API_KEY = 'mmayUu9KKeqv425UyQE84caUdQuOm04ROgO5JKCbih8'

params = { "results": 5 }

response = requests.get(url,params=params)

if response.status_code == 200:
    data = response.json()
    users =data.get("results",[])
    for i, user in enumerate(users,start=1):
        name = f'{user["name"]["first"]} {user["name"]["last"]}'
        email = user["email"]
        print(f'user {i}: {name}, {email}')
else:
    print('fuAPI')