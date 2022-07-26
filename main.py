
from flask import Flask, render_template, request
import requests
import json
app = Flask(__name__)

API_KEY = "f80b0b8d6bceff54dc1427ab93fa1914"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"


@app.route('/', methods = ['GET', 'POST'])
def index():
    
    warsaw = requests.get( BASE_URL + "appid=" + API_KEY + "&q=Warsaw&units=metric&lang=pl").json()
    warsaw_temp=round(warsaw['main']['temp'])
    warsaw_desc=warsaw['weather'][0]['description']
    warsaw_desc=warsaw_desc.capitalize()
    london = requests.get( BASE_URL + "appid=" + API_KEY + "&q=london&units=metric&lang=pl").json()
    london_temp=round(london['main']['temp'])
    london_desc=london['weather'][0]['description']
    london_desc=london_desc.capitalize()
    new_york = requests.get( BASE_URL + "appid=" + API_KEY + "&q=new york&units=metric&lang=pl").json()
    new_york_temp=round(new_york['main']['temp'])
    new_york_desc=(new_york['weather'][0]['description'])
    new_york_desc=new_york_desc.capitalize()
    if request.method == "POST":
        city = request.form['city']
        url = BASE_URL + "appid=" + API_KEY + "&q=" + city+ "&units=metric"    
        
        respone = requests.get(url).json()
        
        temp = respone['main']['temp']
        wind_speed = respone['wind']['speed']
        
        return render_template('result.html', temp=temp, city=city, wind_speed=wind_speed )
    
    return render_template("index.html",  warsaw_temp= warsaw_temp,  london_temp= london_temp,new_york_temp=new_york_temp,new_york_desc=new_york_desc,london_desc=london_desc, warsaw_desc=warsaw_desc)
def result():
    
    if request.method == "POST":
        city = request.form['city']
        url = BASE_URL + "appid=" + API_KEY + "&q=" + city+ "&units=metric"    
        
        respone = requests.get(url).json()
        
        temp = respone['main']['temp']
        wind_speed = respone['wind']['speed']
        
        return render_template('result.html', temp=temp, city=city, wind_speed=wind_speed)