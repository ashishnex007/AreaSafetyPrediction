from flask import Flask,request
app = Flask(__name__)

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC # "Support Vector Classifier"
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
@app.route('/', methods=['GET', 'POST'])
def index():
    area = int(request.form.get('area'))
    sexratio = int(request.form.get('sex_ratio'))
    rcases = int(request.form.get('r_cases'))
    crimes = int(request.form.get('crimes'))
    wineshops = int(request.form.get('wine_shops'))
    menliteracy = int(request.form.get('men_literacy'))
    pornaccess = int(request.form.get('porn_access'))
    pyschcases = int(request.form.get('psych_cases'))
    dessertedarea = float(request.form.get('desserted'))
    ringroads = int(request.form.get('ring_roads'))
    slumareas = float(request.form.get('slum_areas'))
    season = int(request.form.get('season'))
    timeofvisit = int(request.form.get('time_of_visit'))
    p = reg('Area Safety Prediction.csv',["area","sex ratio","r cases","crimes","wine shops","men literacy","porn access","psych cases","desserted area","ring roads","slum areas","season","time of visit"],"outcome",[area,sexratio,rcases,crimes,wineshops,menliteracy,pornaccess,pyschcases,dessertedarea,ringroads,slumareas,season,timeofvisit])
    print("Bot : The outcome is: ",float(p[0]))
    p = classify('Area Safety Prediction.csv',["area","sex ratio","r cases","crimes","wine shops","men literacy","porn access","psych cases","desserted area","ring roads","slum areas","season","time of visit"],"class",[area,sexratio,rcases,crimes,wineshops,menliteracy,pornaccess,pyschcases,dessertedarea,ringroads,slumareas,season,timeofvisit])
    if int(p[0]) == 0:
        print("Area is not safe")
        pr = "Area is not safe"
    elif int(p[0]) == 1:
        print("Area is safe")
        pr = "Area is safe"
    return pr

if __name__ == '__main__':
    app.run(debug=True)