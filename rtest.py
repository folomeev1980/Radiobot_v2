import requests


r=requests.get("http://cs.mipt.ru/python/lessons/lab9.html")
print(r.text)