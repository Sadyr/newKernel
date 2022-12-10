import requests
r = requests.get('https://api.github.com/events')
print(r.json())

url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': "my-app/0.0.1"}
r = requests.get(url, headers=headers)
a = r.headers()
print(a)

