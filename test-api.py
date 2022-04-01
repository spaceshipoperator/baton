#!/bin/python3

import requests
url= "http://debian20220207aa:5000/data"

# list all data rows 
r = requests.get(url)
res = r.json()
print(res)

# post a new row of items
items=[5, 7, 9]
data={ 'items': items }
r = requests.post(url, json=data)
res = r.json()
print(res)

# list all data rows 
r = requests.get(url)
res = r.json()
print(res)

# update an existing row
url= "http://debian20220207aa:5000/data/data1"
items=[3, 6, 5, 7, 9]
data={ 'items': items }
r = requests.put(url, json=data)
res = r.json()
print(res)

# list all data rows 
url= "http://debian20220207aa:5000/data"
r = requests.get(url)
res = r.json()
print(res)
