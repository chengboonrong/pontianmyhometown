from flask import Flask, render_template, request, jsonify, url_for, abort
import requests
import json
import pickle
import numpy as np
import os

# import tensorflow as tf
# global graph
# graph = tf.get_default_graph() 
# # RandomForest model to predict rain
# rain_clf = pickle.load(open('./models/my_rain_model.sav', 'rb'))

app = Flask(__name__)
app.static_folder = 'static'

### openweatherAPI
API_URL = 'http://api.openweathermap.org/data/2.5/weather?q=Pontian,my&appid=e357f3a75f4a8d5c96ccb0742cccdc27&units=metric'
# API_KEY = 'e357f3a75f4a8d5c96ccb0742cccdc27'
# raw_data = requests.get(API_URL).json()
# print(raw_data)
cities = ['benut', 'pontian', 'kukup', 'pekan nanas']
types = ['atm', 'restaurant', 'hotel', 'school']

@app.route('/')
def home():
    raw_data = requests.get(API_URL).json()
    weather_data = [round(raw_data['main']['temp'], 0), raw_data['main']['humidity'], round(raw_data['wind']['speed'] / 1000 * 3600, 1)  , raw_data['visibility'], raw_data['main']['pressure'], raw_data['clouds']['all']]
    data = {str(i): wd for i, wd in enumerate(weather_data)}
    
    #### rainAPI.py ####
    
    # res = requests.post('http://localhost:8001', json = data)
    # print(res.json())
    # cor = res.json()
    
    ####################
    
    with open('./data/pontianCity.json', 'r') as file_:
            data = json.load(file_)
            mapCities = [c for c in data['cities']]
            # print(mapCities[0])

    ### change 'cor' to cor
    return render_template('home.html', raw=raw_data ,data=weather_data, cor='cor', cities=[p for p in cities], mapCities=mapCities)

@app.route('/test')
def test():
    return render_template('index.html')

@app.route('/<city>')
def getCity(city):
    city = ''.join(city.split(' '))
    if os.path.isfile(f'./data/{city}/{city}_restaurant_new.json'):
        with open(f'./data/{city}/{city}_restaurant_new.json', 'r') as file_:
            data = json.load(file_)
            places = [d for d in data]
            # print(places)
            
        return render_template('place.html', cities=[c.capitalize() for c in cities], city=city, city_capital=str(city).capitalize(), placeList=places, length=len(places), types=types)
    
    else:
        abort(404)
        
@app.route('/<city>/<type_>')
def getPlaces(city, type_):
    city = ''.join(city.split(' '))
    # print(city)
    if os.path.isfile(f'./data/{city}/{city}_{type_}_new.json'):
        with open(f'./data/{city}/{city}_{type_}_new.json', 'r') as file_:
            data = json.load(file_)
            places = [d for d in data]
            # print(places)
            
        return render_template('place.html', cities=[c.capitalize() for c in cities], city=city, city_capital=str(city).capitalize(), placeList=places, length=len(places), types=types)
    
    else:
        abort(404)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')