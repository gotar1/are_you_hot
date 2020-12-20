# import modules
from flask import Flask, render_template, redirect, request, jsonify
from lightgbm import LGBMClassifier
import pandas as pd
import numpy as np
import pickle
import os
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from flask_cors import CORS


# Create an instance of Flask
app = Flask(__name__)

# create an engine and connection setup..reflect tables into sqlalchemy ORM ...
engine = create_engine("sqlite:///dataBase/Are_You_Hot.db")
Base = automap_base()
Base.prepare(engine, reflect=True)

################################################## 
# Database Setup
#################################################
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Are_You_Hot.db"
# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
# Hot = create_classes(db)

# upload saved model file
with open(f'./ML_Hot_Model/lgbm_model.pickle', "rb") as f:
    model = pickle.load(f)

# grap feature names from our model
feature_names = model.booster_.feature_name()

# @app.route("/dashboard/")
# def dashboard():
#     return render_template("dashboard.html") 
# @app.route('/')

# def route():
#     """List all available routes"""
#     return (
#         f"Available Routes: <br/>"
#         f"/api/v1.0/hot<br/>"
        # f"/api/v1.0/monthly<br/>"
        # f"/api/v1.0/world<br/>"
    # )
# create a route..
@app.route('/api/v1.0/hot')
def hot():
    ## create session
    session = Session(engine)
    conn = engine.connect()
    df = pd.read_sql("SELECT * FROM hot", conn)
    session.close()
    return df.to_json(orient="records")

# Route to render index2.html template
@app.route("/", methods=["GET", "POST"])
def home():
    """List all available api routes"""
    output_message = ""
    if request.method == "POST":
        sex = str(request.form["sex"])
        eye_color = str(request.form["eye color"])
        distinctive_features = str(request.form["distinctive features"])
        height = float(request.form["height"])
        weight = float(request.form["weight"])
        ratio = weight/height
        age = float(request.form["age"])

        # convert user input into a dataFrame and let columns equal to our data columns..
        data_df = pd.DataFrame(np.array([[sex, eye_color, distinctive_features, ratio, age]]), columns=['sex', 'eye_color', 'distinctive_features', 'ratio(wt/ht)', 'age'])
        
        # convert objects types to numerical.
        data_df['age'] = pd.to_numeric(data_df['age'])
        data_df['ratio(wt/ht)'] = pd.to_numeric(data_df['ratio(wt/ht)'])

        # making user input not case sensitive. since our dataframe features start with capital letter..
        data_df['sex'] = data_df['sex'].str.title()
        data_df['eye_color'] = data_df['eye_color'].str.title()
        data_df['distinctive_features'] = data_df['distinctive_features'].str.title()

        print(data_df)
        print(data_df.dtypes)

        # We use pandas get_dummies to create OneHotEncoder variables
        data = pd.get_dummies(data_df)

        # for loop to use only features corresponding to user input.
        for col in feature_names:
            if col not in data.columns:
                data[col] = 0

        # make our prediction using our model and print corresponding message. 
        result = model.predict(data[feature_names])
        if result == 0:
            output_message = "Hot Hot..It's Getting Hot in Here ^_^"
            
        else:
            output_message = "Looks Like You Have a Good Personality :-("

        print(data)

        # print(feature_names)
    return render_template("index.html", message = output_message)
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html") 
@app.route("/barchart")
def barchart():
    return render_template("barchart.html") 
@app.route("/piechart")
def piechart():
    return render_template("piechart.html") 
if __name__ == "__main__":
    app.run(debug=True)
