from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

app.config.from_pyfile('config.py')

#api end point and key (replace api key)

API_KEY = app.config['API_KEY']
API_URL = "http://api.openweathermap.org/data/2.5/weather"

app.route('/')
def index():
    return render_template('index.html')


@app.route ('/weather', methods=['POST'])

def get_weather():
    city = request.form['city']
    params = {
        'q':city,
        'appid': API_KEY,
        'units': 'metric'
    }

    response = request.get(API_URL, params=params)
    weather_data = response.json()

    if weather_data.get('cod') != 200:
        return render_template('index.html', error=weather_data.get('message'))

    weather = {
        'city': weather_data['name'],
        'temperature': weather_data['main']['temp'],
        'description': weather_data['weather'][0]['description'],
        'icon': weather_data['weather'][0]['icon']
    }

    return render_template('index.html', weather=weather)
       
    if __name__ == '__main__':
        app.run(debug=True)