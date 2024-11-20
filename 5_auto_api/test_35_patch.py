#requests.patch(url,data=None,kwargs)

import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'
payload = {"title":"foo"}
respone = requests.patch(url,json=payload)
print(respone.status_code)
