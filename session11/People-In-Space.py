import requests
 
url = "http://api.open-notify.org/astros.json"
 
r = requests.get(url)
j = r.json()
print(j)
n = j['number']
print(n)