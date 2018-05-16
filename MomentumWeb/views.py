"""
Routes and views for the flask application.
"""

import numpy as np
from datetime import datetime
from flask import request
from MomentumWeb import app
from flask import jsonify
from MomentumWeb.utils import *
from MomentumWeb.constants import *
from MomentumWeb import model

@app.route("/predict", methods=["POST", "GET"])
def predict():
    if request.method == 'POST':
        action = request.form['action']
        time = request.form['time']
        price = request.form['price']

        #TODO
        #add to hist data
        append_row_to_csv(HIST_DATA_PATH, [action, time, price])

        #read last feature
        previous_features = read_last_n_data(HIST_FEATURES_PATH, -1)

        #generate new features
        features = generate_new_features(action, time, price, previous_features)

        #do prediction
        log_dprice_prediction = model.predict(features)

        # transformate predictions
        prediction = price * np.exp(log_dprice_prediction)

        return jsonify(prediction=prediction)

    if request.method == 'GET':
        action = request.args['action']
        time = request.args['time']
        price = request.args['price']

        #TODO
        #add to hist data
        append_row_to_csv(HIST_DATA_PATH, [action, time, price])

        #read last feature
        #previous_features = read_last_n_data(HIST_FEATURES_PATH, -1)

        #generate new features
        #features = generate_new_features(action, time, price, previous_features)

        #do prediction
        #log_dprice_prediction = model.predict(features)

        # transformate predictions
        #prediction = price * np.exp(log_dprice_prediction)

        return jsonify(prediction=130)