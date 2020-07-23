from flask import Flask, render_template, request, jsonify, url_for, abort
import requests
import json
import pickle
import numpy as np
import tensorflow as tf
import os


global graph
graph = tf.get_default_graph() 
# RandomForest model to predict rain
rain_clf = pickle.load(open('./models/my_rain_model.sav', 'rb'))

app = Flask(__name__)
app.static_folder = 'static'

### openweatherAPI
API_URL = 'http://api.openweathermap.org/data/2.5/weather?q=Pontian,my&appid=e357f3a75f4a8d5c96ccb0742cccdc27&units=metric'
# API_KEY = 'e357f3a75f4a8d5c96ccb0742cccdc27'
# raw_data = requests.get(API_URL).json()
# print(raw_data)
placeTypes = ['atm', 'cafe', 'convenience_store', 'pharmacy', 'restaurant', 'school', 'nothing', 'hello']

@app.route('/')
def home():
    raw_data = requests.get(API_URL).json()
    # print(raw_data)
    weather_data = [round(raw_data['main']['temp'], 0), raw_data['main']['humidity'], round(raw_data['wind']['speed'] / 1000 * 3600, 1)  , raw_data['visibility'], raw_data['main']['pressure'], raw_data['clouds']['all']]
    # print(weather_data)

    cor = round(rain_clf.predict(np.array(weather_data).reshape(1, -1))[0], 1)

    with open('./data/pontianCity.txt', 'r') as file_:
            data = json.load(file_)
            mapCities = [c for c in data]
            # print(mapCities[0])

    return render_template('home.html', raw=raw_data ,data=weather_data, cor=cor, types=[p for p in placeTypes], mapCities=mapCities)

@app.route('/test')
def test():
    return render_template('index.html')

@app.route('/<placeType>')
def getPlaces(placeType):
    if os.path.isfile(f'./data/{placeType}.json'):
        with open(f'./data/{placeType}.json', 'r') as file_:
            data = json.load(file_)
            places = [d for d in data]
            # print(places[0]['photo'])



        return render_template('place.html', type=str(placeType).capitalize(), placeList=places, length=len(places))
    
    else:
        abort(404)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')