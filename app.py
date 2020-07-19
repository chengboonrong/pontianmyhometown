from flask import Flask, render_template, request, jsonify, url_for
import requests
import json
import pickle
import numpy as np
import tensorflow as tf


global graph
graph = tf.get_default_graph() 
# RandomForest model to predict flood and rain
flood_clf = pickle.load(open('./models/my_flood_model.sav', 'rb'))
rain_clf = pickle.load(open('./models/my_rain_model.sav', 'rb'))

app = Flask(__name__)
app.static_folder = 'static'

keys = ['apparentTemperature', 'humidity', 'windSpeed', 'visibility', 'pressure']

### openweatherAPI
API_URL = 'http://api.openweathermap.org/data/2.5/weather?q=Pontian,my&appid=e357f3a75f4a8d5c96ccb0742cccdc27&units=metric'
# API_KEY = 'e357f3a75f4a8d5c96ccb0742cccdc27'
# raw_data = requests.get(API_URL).json()
# print(raw_data)

@app.route('/', methods=["GET", "POST"])
def home():
    raw_data = requests.get(API_URL).json()
    # print(raw_data)
    weather_data = [raw_data['main']['temp'], raw_data['main']['humidity'], raw_data['wind']['speed'], raw_data['visibility'], raw_data['main']['pressure'], raw_data['clouds']['all']]
    # print(weather_data)

    cor = rain_clf.predict(np.array(weather_data).reshape(1, -1))[0]
    cof = round(flood_clf.predict(np.array(weather_data).reshape(1, -1))[0], 1)
    prediction = [cor , cof]

    return render_template('home.html', data=raw_data, cor=cor, cof=cof)

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')