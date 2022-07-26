
import requests



API_KEY = "f80b0b8d6bceff54dc1427ab93fa1914"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = 'London'
URL = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
warsaw = requests.get( BASE_URL + "appid=" + API_KEY + "&q=Warsaw&units=metric").json()
warsaw_temp=warsaw['main']['temp']
london = requests.get( BASE_URL + "appid=" + API_KEY + "&q=london&units=metric").json()
london_temp=london['main']['temp']
new_york = requests.get( BASE_URL + "appid=" + API_KEY + "&q=new york&units=metric").json()
new_york_temp=new_york['main']['temp']


print(warsaw_temp)