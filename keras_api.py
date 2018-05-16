from keras.models import load_model
from data_reader import *
from tensorflow import get_default_graph
import numpy as np
import pandas as pd
import flask


# initialize our Flask application and the Keras model
app = flask.Flask(__name__)
model = None
graph = None

def load_keras_model():
    # load the pre-trained Keras model
    global model
    global graph
    model = load_model('trained/LSTM_pt.h5')
    graph = get_default_graph()

def prepare_data(data):
    dataset = pd.DataFrame(data)
    last_price = dataset[2].astype(float).iloc[-1]
    dataset = convert_raw_data(dataset)
    return dataset, last_price


@app.route("/predict", methods=["POST"])
def predict():
    # initialize the data dictionary that will be returned from the
    # view
    data = {"success": False}

    # ensure an image was properly uploaded to our endpoint
    if flask.request.method == "POST":
        req_data = flask.request.get_json()
        dataset, last_price = prepare_data(req_data)
        X, dprice_mean, dprice_std = normalize(dataset)

        x = X.reshape(len(X), 1, 4)
        with graph.as_default():
            pred = model.predict(x)
        prediction = pred[-1]
        predicted_dprice = prediction[0, 0]
        predicted_trend_duration = prediction[0, 1]

        actual_dprice = np.round(last_price + predicted_dprice * dprice_std + dprice_mean, 3)
        actual_trend_duration = np.round(float(np.exp(predicted_dprice)), 3)

        data["price"] = actual_dprice
        data["trend_duration"] = actual_trend_duration
        # indicate that the request was a success
        data["success"] = True

    # return the data dictionary as a JSON response
    return flask.jsonify(data)

if __name__ == "__main__":
    print(("* Loading Keras model and Flask starting server..."
        "please wait until server has fully started"))
    load_keras_model()
    app.run()