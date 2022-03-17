# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 13:54:20 2022

@author: wenbo
"""

import glob
import pandas as pd
import matplotlib.pyplot as plt

csv_paths=glob.glob('./data/*/*.csv')
fig = plt.figure()

for item in csv_paths:
    df=pd.read_csv(item)
    x = df['Time (s)']
    y = df['Relative Conductivity (% IS1)']
    plt.scatter(x,y,marker='.')
    plt.show()
    # plt.savefig(item[:-3]+'png')
    plt.clf()
    # break



