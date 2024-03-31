import requests
latitude = 30.266666
longitude = -97.733330

# office = f"https://api.weather.gov/points/{latitude},{longitude}"
# print(office)

office='EWX'
gridX=156
gridY=91
URL=f"https://api.weather.gov/gridpoints/{office}/{gridX},{gridY}/forecast"
print(URL)

data=requests.get(URL)
data=data.json()
sweater_weather = data["properties"]["periods"][0]['name']
sweater_weather2 = data["properties"]["periods"][0]['temperature']
#print(sweater_weather)
# type(data)  # dict
# print('start')
# for key in data.keys():
#     each_value = data[key]
#     print(each_value, "/n /n")
print()
# key1="properties"
# first_level=data[key1]
# #type(first_level)
# first_level.keys()
# print('start')
# for key in first_level.keys():
#     print("key:", key)
#     print("value:", first_level[key])
# #print(data[key1])
# print("start2")
# key2="periods"
# second_level=first_level[key2]
# key_n="name"
# key_t="temperature"
# for item in second_level:
#     print(item[key_n], item[key_t])


# for i in sweater_weather:
#     print(sweater_weather)
#[sg.Text(sweater_weather)]
#type(data["properties"])
#print(data.keys())

import PySimpleGUI as sg

sg.theme('BluePurple')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Learning Python is fun!')],
            [sg.Text(sweater_weather)],
            [sg.Text(sweater_weather2)],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()