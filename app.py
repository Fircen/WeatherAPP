
from flask import Flask, render_template, request, redirect, url_for
import requests
import json
from datetime import datetime
app = Flask(__name__)
API_KEY = "###"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

def get_weather(city):
    url = BASE_URL + "appid=" + API_KEY + "&q=" + city + "&units=metric"
    respone = requests.get(url).json()
    d = datetime.utcfromtimestamp(respone['dt'] + respone['timezone'])
    d = d.strftime("%b %d %H:%M")
    weather = {
            'city' : city,
            'temperature' : respone['main']['temp'],
            'description' : respone['weather'][0]['description'],
            'icon' : respone['weather'][0]['icon'],
            'time' : d
        } 
    return weather

@app.route('/', methods = ['GET', 'POST'])
def index():
    new_york = get_weather('new york')
    london= get_weather('london')
    warsaw = get_weather('warsaw')

    if request.method == "POST":
        city = request.form['city']
        weather = get_weather(city)
        return render_template('result.html', weather = weather )
    
    return render_template("index.html", new_york = new_york, london = london, warsaw = warsaw)
    
