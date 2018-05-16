"""
The flask application package.
"""
from keras.models import load_model
from flask import Flask
from MomentumWeb.constants import *
app = Flask(__name__)

model = load_model(KERAS_MODEL_PATH)

import MomentumWeb.views
