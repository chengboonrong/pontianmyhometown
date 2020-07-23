from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

with open('./data/pontianCity.json', 'r') as f:
    jsn = json.load(f)
    cities = dict(jsn['cities'])
    # print(dict(jsn['cities']))
    # print(cities)

# with open('atm.json', 'r') as f:
#     jsn = json.load(f)
#     places = jsn
#     # print(len(places))

placeTypes = ['atm', 'cafe', 'convenience_store', 'hotel', 'mall', 'pharmacy', 'restaurant' , 'school']

class City(Resource):
    def get(self):
        return cities

class City_Id(Resource):
    def get(self, city_id):
        city_id = city_id.capitalize()
        return {city_id: cities[city_id]}

class Place(Resource):
       def get(self):
        return {'search_place_types': placeTypes}

class Place_Type(Resource):
    def get(self, place_type):
        with open(f'./data/{place_type}.json', 'r') as f:
            jsn = json.load(f)
            places = jsn
            # print(len(places))

        return {'result': places}

class Home(Resource):
    def get(self):
        pass        

api.add_resource(City, '/city')
api.add_resource(City_Id, '/city/<string:city_id>')
api.add_resource(Place, '/place/')
api.add_resource(Place_Type, '/place/<string:place_type>')
api.add_resource(Home, '/')

if __name__ == '__main__':
     app.run(debug=True, port='5001')