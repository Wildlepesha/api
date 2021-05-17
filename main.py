#! python3
# Weather api
import requests
import json


def api(city):
    api_key = "4fec1cc73d9ce27fcc2771ea45d79129"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}&lang=ru"
    response = requests.get(url)
    x = response.json()
    print(f"""Город: {x['name']}
Погода: {x['weather'][0]['description']}, {x["main"]["temp"]}°С, ощущается как {x["main"]["feels_like"]}°С,\
 максимальная температура сегодня - {x["main"]["temp_max"]}°С   
     """)


api('Moscow')