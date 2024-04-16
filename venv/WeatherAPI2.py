# We are going to construct a web address request
# Send it to a server
# We will get data
# We will transform data
# We will represent or display data
# ETL: Extract, Transform, Load
# Google: weather gov api, https://www.weather.gov/documentation/services-web-api

import requests

office = 'EWX'
latitude = 30.266666  # Get lat to plugin to points url
longitude = -97.733330  # Get long to plugin to points url
# f"https://api.weather.gov/points/{latitude},{longitude}"  # This will get the endpoints used in the below url
gridX = 156
gridY = 91
url = f"https://api.weather.gov/gridpoints/{office}/{gridX},{gridY}/forecast"
# the f in front of the string in url is creating a function string, which means it will take variables in as values
print(url)

# use get url to send a request and get the data back in json
req_data = requests.get(url).json()["properties"]["periods"]
# print(req_data[0]['name'])
# req_data2 = req_data
for data in req_data:
    print(data['name'], data['temperature'])

# weather = []
# for name in req_data:
#     if name == 'name':
#         weather.append(name)

#     print(weather)


# Use the keys ['properties'] and ['periods'] to get the forecast
