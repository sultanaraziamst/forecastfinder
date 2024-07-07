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