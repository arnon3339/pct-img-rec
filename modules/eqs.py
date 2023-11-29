import numpy as np
import scipy as sc
from scipy.integrate import quad
from modules import data

def en_integral_fomular(en, en_in_J, en_out_J):
    e = 1e6 * 1.6e-19 #coulomb
    N_A = 6.022e23 #mol-1
    i_water = 78 #eV
    i_water_J = 78 * e #Jule
    re = 2.82e-15 #m
    me = 9.10e-31 #kg
    c = 3e8 #m/s^2
    Z = 10 #mol-1
    A = 18.0e-3 #kg/mol
    z = 1 #charge
    v = np.sqrt(2*en_in_J / me) #m/s
    beta = v/c
    gamma = 1/np.sqrt(1 - beta**2)

    return 4*np.pi * N_A * re**2 * me*c**2 * Z/A * (z**2/beta**2)
    

def cal_stp(Ek):
    N_A = 6.022e23 #mol-1
    I_water = 78e-6 #MeV
    re = 2.82e-13 #cm
    Z = 10 #mol-1
    A = 18.0 #g/mol
    z = 1 #charge
    mec2 = 0.511 
    m0c2 = 938
    beta = np.sqrt(1 - (1 / ((Ek / m0c2) + 1))**2)
    gamma = 1/np.sqrt(1 - beta**2)

    return 4*np.pi * N_A * re**2 * mec2 * (Z/A) * (1/beta**2) *\
        np.log((2 * mec2 * gamma**2 ** beta**2) / (I_water))

def en_integral(en_in, en_out): 
    stp_data = data.get_stp_data()
    stp_values = stp_data[(stp_data["T"] > en_in) & (stp_data["T"] < en_out)]["STOP(t)"].values
    T_values = stp_data[(stp_data["T"] > en_in) & (stp_data["T"] < en_out)]["T"].values
    return np.trapz(stp_values, T_values)