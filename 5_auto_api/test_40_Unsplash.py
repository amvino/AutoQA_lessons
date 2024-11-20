#Отправьте запрос с вашим ключом API и параметром query=nature. Получите ссылку на случайное изображение природы и выведите её.

import requests


url = "https://api.unsplash.com/photos/random"
API_KEY = 'mmayUu9KKeqv425UyQE84caUdQuOm04ROgO5JKCbih8'

params = {
    "query": "nature",
    "client_id" : API_KEY
}

response = requests.get(url,params=params)

if response.status_code == 200:
    data = response.json()
    img_url = data.get("urls",{}).get("regular")
    if img_url:
        print(f'сслыка на картинку {img_url}')
    else:
        print('f u')
else:
    print('fuAPI')