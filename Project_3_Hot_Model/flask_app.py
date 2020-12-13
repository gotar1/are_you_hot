from flask import Flask, render_template, redirect, request
from xgboost import XGBClassifier
import pandas as pd
import numpy as np
import pickle
import os

# Create an instance of Flask
app = Flask(__name__)


# filename = os.path.abspath(__file__) + os.sep + 'lgbm_model.pickle'

filename = './lgbm_model.pickle'
with open('filename', "rb") as f:
    model = pickle.load(f)

feature_names = model.get_booster().feature_names

# Route to render index.html template
@app.route("/", methods=["GET", "POST"])
def home():
    output_message = ""

    if request.method == "POST":
        sex = float(request.form["sex"])
        eye_color = float(request.form["eye color"])
        hair_color = float(request.form["hair color"])
        distinctive_features = float(request.form["distinctive features"])
        zodiac_sign = float(request.form["zodiac sign"])
        tattoo_body_art = float(request.form["tattoo body art"])
        age = float(request.form["age"])

        # data must be converted to df with matching feature names before predict
        data = pd.DataFrame(np.array([[sex, eye_color, hair_color, distinctive_features, zodiac_sign, tattoo_body_art, Age]]), columns=feature_names)
        result = model.predict(data)
        if result == 0:
            output_message = "Hot Hot..It's Getting Hot in Here ^_^"
        else:
            output_message = "Looks Like You Have a Good Personality :-("
    
    return render_template("../templates/index.html", message = output_message)

if __name__ == "__main__":
    app.run()
