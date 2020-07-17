from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)


API_URL = 'https://api.darksky.net/forecast/81363853dc336450b84e781b96c555d4/'

@app.route('/', methods=["GET", "POST"])
def home():
    # if request.method == 'POST':
    #     latlong = request.get_json()
        # print(latlong)
        # try:
        #     weather_data = requests.get(API_URL + f"{latlong['lat']},{latlong['long']}").json()
        #     print(weather_data['timezone'], weather_data['currently'])
        # except:
        #     print('err')

        # return render_template('home.html', data=weather_data['timezone'])

    return render_template('index.html')

if __name__ == '__main__':
   app.run(host='0.0.0.0')