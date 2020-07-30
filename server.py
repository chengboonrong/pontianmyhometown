from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

with open('./data/pontianCity.json', 'r') as f:
    jsn = json.load(f)
    cities = [c for c in jsn['cities']]
    print(cities[0])
    # print(cities)

# with open('atm.json', 'r') as f:
#     jsn = json.load(f)
#     places = jsn
#     # print(len(places))

cityList = ['benut', 'pontian', 'kukup', 'pekannanas']
typeList = ['atm', 'cafe', 'convenience_store', 'hotel', 'mall', 'pharmacy', 'restaurant' , 'school']
# keyword = ['']

class City(Resource):
    def get(self):
        return cities

# class City_Id(Resource):
#     def get(self, city_id):
#         city_id = city_id.capitalize()
#         return {city_id: cities['city']}

class Place(Resource):
       def get(self):
        return {'search_place_types': typeList}

class Place_City(Resource):
    def get(self, city, type_):
        with open(f'./data/{city}/{city}_{type_}_new.json', 'r') as f:
            jsn = json.load(f)
            places = jsn
            # print(len(places))

        return {'result': places}

class Home(Resource):
    def get(self):
        pass        

api.add_resource(City, '/city')
# api.add_resource(City_Id, '/<string:city_id>')
api.add_resource(Place, '/city/place/')
api.add_resource(Place_City, '/<string:city>/<string:type_>')
api.add_resource(Home, '/')

if __name__ == '__main__':
     app.run(debug=True, port='5001')