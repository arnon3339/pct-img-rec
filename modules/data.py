import pandas as pd

def get_stp_data():
    return pd.read_csv("./data/stopping_power.txt", delimiter=',')