import requests
# from pprint import pprint
url = "https://us1.locationiq.com/v1/nearby.php"
data = {
        'key': '78f81c3fc2a001',
        'lat':  '5.416667', 
        'lon': '6.966667',
        'tag': 'atm',
        'radius': 2000,
        'format': 'json'
        }
response = requests.get(url, params=data)
print(response.text)
