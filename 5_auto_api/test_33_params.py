import requests

#1
url = 'https://jsonplaceholder.typicode.com/posts'
params = {"userId":1}
response = requests.get(url,params=params)
print(response.url)

#2
url = 'https://jsonplaceholder.typicode.com/posts'
payload = {"title":"foo","body":"bar","userId":1}
respone = requests.post(url,json=payload)
print(respone.status_code)
