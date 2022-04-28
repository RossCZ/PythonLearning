import requests as rq

r = rq.get('https://www.google.com/')
print(r.content)
