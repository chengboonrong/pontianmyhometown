from flask import Flask, render_template, request, jsonify, url_for, abort
import pickle
import numpy as np

import tensorflow as tf
global graph
graph = tf.get_default_graph() 
# RandomForest model to predict rain
rain_clf = pickle.load(open('./models/my_rain_model.sav', 'rb'))

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    if request.is_json:

        # Parse the JSON into a Python dictionary
        req = request.get_json()

        # Print the dictionary
        print(req)
        
        data = [v for v in req.values()]
        cor = round(rain_clf.predict(np.array(data).reshape(1, -1))[0], 1)
        

        # Return a string along with an HTTP status code
        return str(cor), 200


if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port='8001')