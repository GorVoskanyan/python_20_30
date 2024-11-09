import json
import requests

# url = 'https://www.google.com'
# response = requests.get(url)
# print(response.status_code)
# print(response.text)

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
# data = json.loads(requests.get(url).text)

data = requests.get(url).json()
print(type(data))
# for key, value in data.items():
#     print(key, '->', value)

time = data['time']
print(time)
print('Current:')
for key, value in data['bpi'].items():
    print(f'BTC|{key} -> {value['rate']}')