"""
Routes and views for the flask application.
"""

from flask import request
from MomentumWeb import app
from flask import jsonify
from MomentumWeb.utils import *

@app.route("/predict", methods=["POST", "GET"])
def predict():
    if request.method == 'POST':
        action = request.form['action']
        time = request.form['time']
        price = request.form['price']

        prediction = predict_price(action, time, price)

        return jsonify(prediction=prediction)

    if request.method == 'GET':
        action = request.args['action']
        time = request.args['time']
        price = request.args['price']

        prediction = predict_price(action, time, price)

        return jsonify(prediction=prediction)