# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 10:20:39 2020

@author: Sai Pavan Velidandla
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC 
def reg(file,impacts,outcome,inps):
    data = pd.read_csv(file)
    X = data[impacts]
    Y = data[outcome]
    linear_regressor = LinearRegression()
    linear_regressor.fit(X, Y)
    nx = [inps]
    pred = linear_regressor.predict(nx)
    return pred

def classify(file,impacts,outcome,inps):
    data = pd.read_csv(file)
    X = data[impacts]
    Y = data[outcome]
    Y=Y.round()
    clf = SVC(kernel='linear') 
    clf.fit(X,Y)
    nx = [inps]
    pred = clf.predict(nx)
    return pred

area=int(input("area: "))
sexratio = int(input("sexratio: "))
rcases = int(input("rcases: "))
crimes = int(input("crimes: "))
wineshops = int(input("wineshops: "))
menliteracy = int(input("menliteracy: "))
pornaccess = int(input("pornaccess: "))
pyschcases = int(input("pyschcases: "))
dessertedarea = float(input("dessertedarea: "))
ringroads = int(input("ringroads: "))
slumareas = float(input("slumareas: "))
season = int(input("season: "))
timeofvisit = int(input("timeofvisit: "))
ch = int(input("What do you want to perform?\n1. Regression\n2. Classification\nEnter your choice: "))
if ch == 1:
    p = reg('Area Safety Prediction.csv',["area","sex ratio","r cases","crimes","wine shops","men literacy","porn access","psych cases","desserted area","ring roads","slum areas","season","time of visit"],"outcome",[area,sexratio,rcases,crimes,wineshops,menliteracy,pornaccess,pyschcases,dessertedarea,ringroads,slumareas,season,timeofvisit])
    print("Bot : The outcome is: ",float(p[0]))
elif ch == 2:
    p = classify('Area Safety Prediction.csv',["area","sex ratio","r cases","crimes","wine shops","men literacy","porn access","psych cases","desserted area","ring roads","slum areas","season","time of visit"],"class",[area,sexratio,rcases,crimes,wineshops,menliteracy,pornaccess,pyschcases,dessertedarea,ringroads,slumareas,season,timeofvisit])
    if int(p[0]) == 0:
        print("Area is not safe")
    elif int(p[0]) == 1:
        print("Area is safe")
else:
    print("Invalid choice!")