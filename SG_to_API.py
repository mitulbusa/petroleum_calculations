# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 11:15:02 2020

@author: MITUL BUSA
"""
from matplotlib import pyplot as plt
import numpy as np

SG = float(input("Enter Specific Gravity"))
API = 141.5/SG - 131.5
print("API: ",round(API,4))

ask = input("Show Plot of SG vs API (y or n): ")
if ask.lower() == "y":
    while 1 == 1:
        ll = float(input("SG starts from(should be greater than 0): "))
        if ll>0:
            break
        if ll<= 0:
            print("SG should be greter than 0")
    while 1==1:
        ul = float(input("SG ends(should not grater than 1): "))
        if ul>ll:
            break
        print("end should be greter than start")
    while 1==1:
        steps = int(input("how many steps you want(upto 1000 is recommanded): "))
        if steps>0:
            break
        print("steps should be greater than 0")
    x=[]
    y=[]
    for i in np.linspace(ll,ul,steps):
        x.append(i)
        api = 141.5/i -131.5
        y.append(api)

    plt.plot(x,y)
    plt.xlabel("SG")
    plt.ylabel("API = 141.5/SG - 131.5")
    plt.show()