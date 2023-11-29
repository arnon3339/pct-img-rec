import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib import font_manager
from matplotlib.ticker import (MultipleLocator,
                               FormatStrFormatter,
                               AutoMinorLocator)
from os import path
from modules import data
import numpy as np

OUTPUT_DIR = "./output"
TIMES_FONT_PATH = r"./font/Times-New-Roman/"
# TIMES_REG = font_manager.FontProperties(TIMES_FONT_PATH + r"times new roman.ttf")
TIMES_BOLD = font_manager.FontProperties(fname=TIMES_FONT_PATH + r"times-new-roman-bold.ttf")
FNAME = TIMES_FONT_PATH + r"times-new-roman-bold.ttf"
FONT_SIZE = 28

def plot_stp(data, stp_data):
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.plot(stp_data["T"], stp_data["STOP(e)"], linewidth=3, label="PSTAR e")
    ax.plot(stp_data["T"], stp_data["STOP(t)"], linewidth=3, label="PSTAR p")
    ax.set_xlabel("Energy (MeV)", fontproperties=TIMES_BOLD, fontsize=FONT_SIZE, labelpad=6)
    ax.set_ylabel(r"Stopping power (cm$\mathrm{^2}$/g)", fontproperties=TIMES_BOLD, fontsize=FONT_SIZE, labelpad=6)
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.tick_params(axis='both', pad=10, width=2.0, length=14, direction='in', labelfontfamily=FNAME)
    ax.tick_params(axis='both', which='minor', pad=10, width=1, length=8, direction='in', labelfontfamily=FNAME)
    ax.set_xscale('log')
    for x in ax.get_xticklabels():
        x.set_fontproperties(TIMES_BOLD)
        x.set_fontsize(FONT_SIZE)
    for y in ax.get_yticklabels():
        y.set_fontproperties(TIMES_BOLD)
        y.set_fontsize(FONT_SIZE)
    leg = ax.legend(prop={"fname": FNAME, "size": FONT_SIZE})
    leg.get_frame().set_edgecolor('black')
    leg.get_frame().set_boxstyle('Square', pad=0.3)
    plt.savefig(path.join(OUTPUT_DIR, "stopping-power.png"), bbox_inches='tight', dpi=300)
    plt.show()

def plot_int_stp(en_in, en_out):
    stp_data = data.get_stp_data()
    stp_values = stp_data[(stp_data["T"] >= en_in) & (stp_data["T"] <= en_out)]["STOP(t)"].values
    T_values = stp_data[(stp_data["T"] >= en_in) & (stp_data["T"] <= en_out)]["T"].values
    concat_data = np.concatenate((T_values.reshape(-1, 1), (1/stp_values).reshape(-1, 1)), axis=1)
    data_2 = data.gen_new_data(concat_data)
    # print(data_2)
    fig, ax = plt.subplots(figsize=(14, 10))
    # print(np.concatenate((T_values.reshape(-1, 1), (1/stp_values).reshape(-1, 1)), axis=1))
    ax.scatter(data_2[:, 0], data_2[:, 1], s=2, c='blue', label="new 1/S")
    ax.scatter(T_values, 1/stp_values, s=2, c='red', label="1/S")
    ax.set_xlabel("Energy (MeV)", fontproperties=TIMES_BOLD, fontsize=FONT_SIZE, labelpad=6)
    ax.set_ylabel(r"1/Stopping power (g/cm$\mathrm{^2}$)", fontproperties=TIMES_BOLD, fontsize=FONT_SIZE, labelpad=6)
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.tick_params(axis='both', pad=10, width=2.0, length=14, direction='in', labelfontfamily=FNAME)
    ax.tick_params(axis='both', which='minor', pad=10, width=1, length=8, direction='in', labelfontfamily=FNAME)
    ax.set_xlim([T_values.min(), T_values.max()])
    # ax.set_xscale('log')
    for x in ax.get_xticklabels():
        x.set_fontproperties(TIMES_BOLD)
        x.set_fontsize(FONT_SIZE)
    for y in ax.get_yticklabels():
        y.set_fontproperties(TIMES_BOLD)
        y.set_fontsize(FONT_SIZE)
    leg = ax.legend(prop={"fname": FNAME, "size": FONT_SIZE})
    leg.get_frame().set_edgecolor('black')
    leg.get_frame().set_boxstyle('Square', pad=0.3)
    plt.savefig(path.join(OUTPUT_DIR, "stopping-power.png"), bbox_inches='tight', dpi=300)
    plt.show()