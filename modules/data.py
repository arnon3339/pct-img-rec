import pandas as pd
import numpy as np
import math

def get_stp_data():
    return pd.read_csv("./data/stopping_power.txt", delimiter=',')

def gen_new_data(data, dE = 0.01):
    new_data = []
    for i in range(len(data) - 1):
        new_data_2 = []
        bound_x = [0, data[i + 1, 0] - data[i, 0]]
        bound_y = [0, data[i + 1, 1] - data[i , 1]]
        dydx = bound_y[1]/bound_x[1]
        iter_range = np.linspace(0, bound_x[1], num=math.ceil(bound_x[1]/dE))
        for dd in iter_range:
            new_data_2.append([data[i, 0] + dd, dydx*dd + data[i, 1]])
        new_data += new_data_2
    return np.asarray(new_data)

def expt_csv(data):
    df = pd.DataFrame({"T": data[:, 0], "STOP(t)": data[:, 1]})
    df.to_csv("./output/data/new_data.csv", index=None)