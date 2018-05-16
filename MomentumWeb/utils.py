import pandas as pd
import numpy as np
import csv
from MomentumWeb.constants import *
from MomentumWeb import model

def read_last_n_data(path_to_hist_data, look_back, columns=None):
    dt = pd.read_csv(path_to_hist_data, names=columns, skiprows=-look_back)
    return dt.values


def append_row_to_csv(path_to_hist_data, row):
    with open(path_to_hist_data, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(row)

def generate_new_features(action, time, price, previous_time, previous_price, previous_accumulative_features):
    #TODO convert time to numerical type
    previous_is_signal_first = previous_accumulative_features[0]
    previous_signal_type = previous_accumulative_features[1]
    previous_latancy = previous_accumulative_features[2]
    previous_trend_duration = previous_accumulative_features[3]
    previous_signal_counter = previous_accumulative_features[4]
    previous_d_price = previous_accumulative_features[5]
    previous_trend_gap = previous_accumulative_features[6]
    previous_d_trend_price = previous_accumulative_features[7]


    signal = {"TrendHigh": 1,
          "TrendLow": -1,
          "IlsHigh": 1,
          "IlsLow": -1}
    signal_type = signal[action]
    is_signal_first = 1 if signal_type != previous_signal_type else 0
    latancy = time - previous_time
    trend_duration = 0 if is_signal_first == 1 else previous_trend_duration + latancy
    signal_counter = 0 if is_signal_first == 1 else previous_signal_counter + 1
    d_price = price - previous_price
    trend_gap = d_price if is_signal_first == 1 else previous_trend_gap
    d_trend_price = d_price if is_signal_first == 1 else previous_d_trend_price + d_price
    #TODO Check accumulative features
    new_accumulative_fatures = [
        is_signal_first,
        signal_type,
        latancy,
        trend_duration,
        signal_counter,
        d_price,
        trend_gap,
        d_trend_price
    ]
    return new_accumulative_fatures

def transform_batch(batch_of_accumulative_features):
    #TODO Compute Logs and mornalizations and return batch
    return None

def predict_price(action, time, price):
    append_row_to_csv(HIST_DATA_PATH, [time, action, price])

    # read last feature
    previous_features = read_last_n_data(HIST_FEATURES_PATH, -1)
    previous_signal = read_last_n_data(HIST_DATA_PATH, -1)
    previous_time = previous_signal[0]
    previous_price = previous_signal[2]
    # generate new features
    features = generate_new_features(action, time, price, previous_time, previous_price, previous_features)

    # do prediction

    #read batch of accumulative features
    batch_of_accumulatve_features = read_last_n_data(HIST_FEATURES_PATH, -TIMESTEPS)

    batch_normalized_features = transform_batch(batch_of_accumulatve_features)

    log_dprice_prediction = model.predict(batch_normalized_features)

    # transformate predictions
    prediction = price * np.exp(log_dprice_prediction)
    return prediction