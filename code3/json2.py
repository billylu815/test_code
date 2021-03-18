import json
import urllib.request, urllib.parse, urllib.error
import ssl

# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1173077.json'

print('Retriving url')
uh = urllib.request.urlopen(url)
data = uh.read()
js = json.loads(data)

acc = 0
for item in js['comments']:
    num = int(item['count'])
    acc+=num
print(acc)

'''
js = json.loads(data)
data = 
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]

info = json.loads(data)
print('User count:', len(info))

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])
'''