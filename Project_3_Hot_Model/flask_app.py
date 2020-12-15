from flask import Flask, render_template, redirect, request
from xgboost import XGBClassifier
import pandas as pd
import numpy as np
import pickle
import os

# Create an instance of Flask
app = Flask(__name__)


# filename = os.path.abspath(__file__) + os.sep + 'lgbm_model.pickle'
# model = pickle.load(open(filename, 'rb'))
with open(f'./Project_3_Hot_Model/lgbm_model.pickle', "rb") as f:
    model = pickle.load(f)

# filename = './Project_3/lgbm_model.pickle'
# with open('filename', "rb") as f:
#     model = pickle.load(f)

feature_names = model.Booster().feature_name()

# Route to render index.html template
@app.route("/", methods=["GET", "POST"])
def home():
    output_message = ""

    if request.method == "POST":
        sex = str(request.form["sex"])
        # eye_color = float(request.form["eye color"])
        # hair_color = float(request.form["hair color"])
        distinctive_features = str(request.form["distinctive features"])
        # zodiac_sign = float(request.form["zodiac sign"])
        height = float(request.form["height"])
        weight = float(request.form["weight"])
        ht_wt_ratio = float(height/weight)
        # tattoo_body_art = float(request.form["tattoo body art"])
        age = float(request.form["age"])

        # data must be converted to df with matching feature names before predict
        data = pd.DataFrame(np.array([[sex, distinctive_features, ht_wt_ratio, age]]), columns=feature_names)
        result = model.predict(data)
        if result == 0:
            output_message = "Hot Hot..It's Getting Hot in Here ^_^"
        else:
            output_message = "Looks Like You Have a Good Personality :-("
    
    return render_template("index.html", message = output_message)

if __name__ == "__main__":
    app.run(debug=True)
