from flask_api import FlaskAPI, status, exceptions
from flask import request, url_for
import pandas as pd 
import numpy as np
import tensorflow as tf
from flask_ngrok import run_with_ngrok
from keras.models import load_model


global graph
graph = tf.get_default_graph() 

app = FlaskAPI(__name__)
run_with_ngrok(app)   #starts ngrok when the app is run

# parameters: 'avgtempC', 'sunHour', 'humidity',
#             'windspeedKmph', 'visibility', 'pressure', 'cloudcover',
# predict:    'rain', 'flood', 'precipMM'

## sample data
# {
#     "avgtempC": 25, 				# celcius
#     "sunHour": 7.4, 				# hour 
#     "humidity": 84.75, 			# percentage
#     "windspeedKmph": 4.62, 	# speed
#     "visibility": 9.00, 		# kilometres
#     "pressure": 1009.00, 		# millibars
#     "cloudcover": 61.4 			# percentage
# }

## use this code to test
# curl "http://ecd39003a74b.ngrok.io/" \
#     -X POST \
#     -H 'content-type: application/json' \
#     -d ' {
#      "avgtempC": 25,
#      "sunHour": 7.4,
#      "humidity": 84.75,
#      "windspeedKmph": 4.62,
#      "visibility": 9.00,
#      "pressure": 1009.00,
#      "cloudcover": 61.4
# }'

# curl "http://1e926e81969a.ngrok.io/rainfall" \
#     -X POST \
#     -H 'content-type: application/json' \
#     -d ' {
# 			"data": [0.11344538, 0.07563025, 0.02521008] 
# 		}'

histories = []

import pickle
# RandomForest model to predict flood and rain
flood_clf = pickle.load(open('flood_model.sav', 'rb'))
rain_clf = pickle.load(open('rain_model.sav', 'rb'))

rainfall_model = load_model('lstm-v3-1.h5')
rainfall_model.compile(loss='mean_squared_error', optimizer='adam')

# A route to return all of the available entries in our catalog.
@app.route('/', methods=['GET', 'POST'])
def get_results():
	if request.method == 'POST':
	    posted_data = request.get_json()

	    data = []
	    for item in posted_data.items():
	        data.append(item[1])

	    rain_Result = rain_clf.predict(np.array(data).reshape(1, -1))
	    flood_Result = flood_clf.predict(np.array(data).reshape(1, -1))

	    posted_data['chanceofrain'] = round(rain_Result.tolist()[0], 1)
	    posted_data['chanceofflood'] = round(flood_Result.tolist()[0], 1)
	    histories.append(posted_data)

	    return {'rain': posted_data['rain'], 'flood': posted_data['flood']}
	    
	# if method == GET
	return histories

@app.route('/rainfall', methods=['GET', 'POST'])
def get_rainFall():
	if request.method == 'POST':
		posted_data = request.get_json()
		
		data = []
		for item in posted_data.items():
			data.append(item[1])
			# print(item)

		with graph.as_default():
		  predict = rainfall_model.predict(np.array(data).reshape(1, 1, 3))
		
		posted_data['predicted_rainfall'] = predict.tolist()[0][0] 
		print(data, predict[0][0])

		return {'data': posted_data}

	return 'done'

app.run()