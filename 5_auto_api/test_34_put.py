#requests.put(url,data=None, kwargs)
import requests


url = 'https://jsonplaceholder.typicode.com/posts/1'
payload = {"id":1,"title":"foo","body":"bar","userId":1}
respone = requests.put(url,json=payload)
print(respone.status_code)
