#requests.delete(url,kwargs)

import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'
respone = requests.delete(url)
print(respone.status_code)
