# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 15:06:12 2020

@author: MITUL BUSA
"""
from matplotlib import pyplot as plt
import numpy as np

API = float(input("Enter API Gravity"))
SG = 141.5 / (API + 131.5)
print("SG: ",round(SG,4))

ask = input("Show Plot of API vs SG (y or n): ")
if ask.lower() == "y":
    while 1 == 1:
        ll = float(input("API starts from(Should be positive): "))
        if ll>=0:
            break
        if ll< 0:
            print("API should be greter than 0")
    while 1 == 1:
        ul = float(input("API ends(should be grater than start): "))
        if ul > ll:
            break
        print("end limit should be greater than start")
    while 1==1:
        steps = int(input("how many steps you want(upto 1000 is recommanded): "))
        if steps >= 0:
            break
        print("steps should be positive")
    x=[]
    y=[]
    for i in np.linspace(ll,ul,steps):
        x.append(i)
        sg = 141.5 / (i+131.5)
        y.append(sg)

    plt.plot(x,y)
    plt.xlabel("API")
    plt.ylabel("SG = 141.5 / (API+131.5)")
    plt.show()