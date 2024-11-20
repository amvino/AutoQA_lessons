#Сделайте GET-запрос и выведите шутку в формате:
#<setup>
#<punchline>.

import requests

url = "https://official-joke-api.appspot.com/random_joke"
response = requests.get(url)


if response.status_code ==200:
    joke = response.json()
    setup = joke.get("setup")
    punchline = joke.get("punchline")

    if setup and punchline:
        print(f'{setup}\n{punchline}')
    else:
        print('Шутка не содержит данные')
else:
    print('ПОшел на выход не работает твой говнокод')
