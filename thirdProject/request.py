import requests 
import json

URL = "http://127.0.0.1:8000/stucreate/"

# python data
data = {
    'name': 'Radha',
    'roll': '01',
    'city': 'India'
}

# python data converts into json using dumps
json_data = json.dumps(data)

# request by post to send data to backend
# get response in r variable
r = requests.post(url=URL, data = json_data)

# extract data
data = r.json()
print(data)