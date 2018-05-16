"""
The flask application package.
"""
from keras.models import load_model
from tensorflow import get_default_graph
from flask import Flask
app = Flask(__name__)

model = load_model('trained/LSTM_pt.h5')
graph = get_default_graph()

import MomentumWeb.views
