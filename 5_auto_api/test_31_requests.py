import requests


#отправка get запроса
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
print(response.status_code) #код состояний HTTP
print(response.headers) #получает заголовки ответа сервера.
print(response.json()) #превращает json ответ в python список или словарь
print(response.text) #ответ сервера в виде строки