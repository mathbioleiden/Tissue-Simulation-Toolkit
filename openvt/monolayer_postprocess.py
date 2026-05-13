import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import pdb
# tst_data2=pd.read_csv('monolayer-type1_wo_apoptosis/tst.csv')
tst_data=pd.read_csv('monolayer-type1_beta_0.0/tst.csv')

cell_no_flag=True
if cell_no_flag:
    cell_number_data= tst_data.groupby("time (MCS)")["cell id"].max()
    # cell_number_data2= tst_data2.groupby("time (MCS)")["cell id"].max()
    fig, ax = plt.subplots()
    time_data=cell_number_data.index /86 # Converting MCS to time unit T
    number_data =cell_number_data.values
    # time_data2=cell_number_data2.index /86 # Converting MCS to time unit T
    # number_data2 =cell_number_data2.values
    plt.plot(time_data, number_data)
    # plt.plot(time_data2*10, number_data2)
    ax.set_xscale('linear')
    ax.set_yscale('log')
    ax.grid()
    plt.xlabel('Time (T)')
    plt.ylabel('Number of cells')
    # ax.set_xlim(0,120)
    ax.set_ylim(1,1e5)
    # plt.show()

diameter_flag=True
if diameter_flag:
    fig, ax = plt.subplots()
    Total_area= tst_data.groupby("time (MCS)")["area (px^2)"].sum()
    # Width= tst_data.groupby("time (MCS)")["com_1 (px)"].max() - tst_data.groupby("time (MCS)")["com_1 (px)"].min()
    Diameter= np.sqrt(Total_area/3.14159265)*2 # in px
    time_data=Total_area.index /86
    # pdb.set_trace()
    plt.plot(time_data, Diameter)
    plt.xlabel('Time (T)')
    plt.ylabel('Diameter (px^2)')
    # plt.plot(time_data, Width)
    plt.show()


min_cell_size_flag=False
if min_cell_size_flag:
    fig, ax = plt.subplots()
    min_area= tst_data.groupby("time (MCS)")["area (px^2)"].min()
    # Width= tst_data.groupby("time (MCS)")["com_1 (px)"].max() - tst_data.groupby("time (MCS)")["com_1 (px)"].min()
    time_data=min_area.index /86
    # pdb.set_trace()
    plt.plot(time_data, min_area)
    plt.xlabel('Time (T)')
    plt.ylabel('Min cell area (px^2)')
    ax.grid()
    # plt.plot(time_data, Width)
    plt.show()
