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

### openweatherAPI
API_URL = 'http://api.openweathermap.org/data/2.5/weather?q=Pontian,my&appid=e357f3a75f4a8d5c96ccb0742cccdc27&units=metric'
# API_KEY = 'e357f3a75f4a8d5c96ccb0742cccdc27'
# raw_data = requests.get(API_URL).json()
# print(raw_data)

@app.route('/')
def home():
    raw_data = requests.get(API_URL).json()
    # print(raw_data)
    weather_data = [round(raw_data['main']['temp'], 0), raw_data['main']['humidity'], raw_data['wind']['speed'], raw_data['visibility'], raw_data['main']['pressure'], raw_data['clouds']['all']]
    # print(weather_data)

    cor = round(rain_clf.predict(np.array(weather_data).reshape(1, -1))[0], 1)

    return render_template('home.html', raw=raw_data ,data=weather_data, cor=cor)

@app.route('/test')
def test():
    return render_template('index.html')

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')