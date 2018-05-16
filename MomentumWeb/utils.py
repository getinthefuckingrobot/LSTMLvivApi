import pandas as pd
import csv


def read_last_n_data(path_to_hist_data, look_back, columns=None):
    dt = pd.read_csv(path_to_hist_data, names=columns, skiprows=-look_back)
    return dt.values


def append_row_to_csv(path_to_hist_data ,row):
    with open(path_to_hist_data, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(row)

def generate_new_features(action, time, price, previous_accumulative_features):
    previous_is_signal_first = previous_accumulative_features[0]
    previous_signal_type = previous_accumulative_features[1]
    previous_latancy = previous_accumulative_features[3]
    previous_trend_duration = previous_accumulative_features[4]
    previous_signal_counter = previous_accumulative_features[5]
    previous_d_price = previous_accumulative_features[6]
    previous_d_trend_price = previous_accumulative_features[7]
    #TODO Construct new row of accumulative features
    new_accumulative_fatures = None
    return new_accumulative_fatures

def transform_batch(batch_of_accumulative_features):
    #TODO Compute Logs and mornalizations
    return None