import requests
import math
import datetime
from states import *

filename = 'weatherdata.txt'
with open(filename, 'a') as file_object:
    file_object.write(f"\t\t\t\t\t\t{'-' * 15}SEARCH HISTORY...{'-' * 15}\n")


def info_tech(shadow_location):
    """user input, file storage"""
    shadow_date_time = datetime.datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
    shadow_api_key = '87d845b0b6cf29baa1a73cc34b067a95'
    shadow_url = f"https://api.openweathermap.org/data/2.5/weather?q={shadow_location}&appid={shadow_api_key}"
    shadow_api_link = requests.get(shadow_url)
    shadow_data = shadow_api_link.json()
    shadow_description = shadow_data['weather'][0]['description']
    shadow_temp = shadow_data['main']['temp']
    shadow_temp_f = math.floor((shadow_temp * 1.8) - 459.67)
    shadow_temp_c = math.floor((shadow_temp_f - 32) * 5 / 9)
    shadow_temp_feel = data['main']['feels_like']
    shadow_temp_feel = math.floor((shadow_temp_feel * 1.8) - 459.67)
    shadow_temp_feel = math.floor((shadow_temp_feel - 32) * 5 / 9)
    print(f"Weather Stats for: {shadow_location} Date-Time: {shadow_date_time}")
    print(f"Weather: {shadow_description}\ntemperature: {shadow_temp_f}{chr(176)}F "
          f"or {shadow_temp_c}{chr(176)}C\nFeels like: {shadow_temp_feel}{chr(176)}C\n")
    filename = 'weatherdata.txt'
    with open(filename, 'a') as file_object:
        file_object.write(f"Weather Stats for: {shadow_location} Date-Time: {shadow_date_time}")
        file_object.write(f"Weather: {shadow_description}\ntemperature: {shadow_temp_f}degreeF "
                          f"or {shadow_temp_c}degreeC\nFeels like: {shadow_temp_feel}degreeC\n\n\n")


date_time = datetime.datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
list_1 = []
list_2 = ['Weather Stats for', 'Date-Time', 'Weather', 'temperature', 'Feels like']
dict_1 = {}

for i in states:
    API_key = '87d845b0b6cf29baa1a73cc34b067a95'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={i}&appid={API_key}"
    api_link = requests.get(url)
    data = api_link.json()
    description = data['weather'][0]['description']
    temp = data['main']['temp']
    temp_f = math.floor((temp * 1.8) - 459.67)
    temp_c = math.floor((temp_f - 32) * 5 / 9)
    temp_feel = data['main']['feels_like']
    temp_feel = math.floor((temp_feel * 1.8) - 459.67)
    temp_feel = math.floor((temp_feel - 32) * 5 / 9)
    str_1 = f"{temp_f}{chr(176)}F or {temp_c}{chr(176)}C"
    str_2 = f"{temp_feel}{chr(176)}C"

    list_3 = [i.upper(), date_time, description, str_1, str_2]
    dict_3 = {}
    for j in range(0, 5):
        key_0 = list_2[j]  # ['Weather Stats for', 'Date-Time', 'Weather', 'temperature', 'Feels like']
        value_0 = list_3[j]  # [i.upper(), date_time, description, str_1, str_2]
        dict_1[key_0] = value_0
        dict_3 = dict_1.copy()

    list_1.append(dict_3)
"""final printing"""
for i in range(0, len(list_1) - 1):
    dict_2 = list_1[i]
    c = dict_2.keys()
    c = list(c)
    print(f"{c[0]}: {dict_2[c[0]]} {c[1]}: {dict_2[c[1]]}")
    print(f"{c[2]}: {dict_2[c[2]]}\n{c[3]}: {dict_2[c[3]]}\n{c[4]}: {dict_2[c[4]]}\n")

for i in states:
    print(i)
while True:
    resp1 = input("search any other state or city: ")
    info_tech(resp1)
