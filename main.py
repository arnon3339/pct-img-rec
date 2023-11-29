from modules import eqs, myplot as plot, data
import numpy as np

if __name__ == "__main__":
    stp_data = data.get_stp_data()
    new_data = data.gen_new_data(np.concatenate(
        (stp_data["T"].values.reshape(-1, 1),
        stp_data["STOP(t)"].values.reshape(-1, 1)),
        axis=1
    ))
    data.expt_csv(new_data)