from flask import Flask, render_template, redirect, request
from sklearn.feature_extraction.text import CountVectorizer
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
import pandas as pd
import numpy as np
import pickle
import os

# Create an instance of Flask
app = Flask(__name__)

with open(f'./Project_3_Hot_Model/lgbm_model.pickle', "rb") as f:
    model = pickle.load(f)

# with open(f'./Project_3_Hot_Model/xgb_model.pickle', "rb") as f:
#     model = pickle.load(f)

# model_columns = model.columns
# filename = './Project_3/lgbm_model.pickle'
# with open('filename', "rb") as f:
#     model = pickle.load(f)

feature_names = model.booster_.feature_name()
# feature_names = model.get_booster().feature_names
# print(feature_names)

# Route to render index.html template
@app.route("/", methods=["GET", "POST"])
def home():
    output_message = ""
    # cv = CountVectorizer()
    if request.method == "POST":
        sex = str(request.form["sex"])
        eye_color = str(request.form["eye color"])
        distinctive_features = str(request.form["distinctive features"])
        height = float(request.form["height"])
        weight = float(request.form["weight"])
        ratio = weight/height
        age = float(request.form["age"])

        # , columns=['sex', 'eye_color', 'distinctive_features', 'zodiac_sign', 'ratio(wt/ht', 'age']
        # , columns=feature_names
        # data must be converted to df with matching feature names before predict
        data_df = pd.DataFrame(np.array([[sex, eye_color, distinctive_features, ratio, age]]), columns=['sex', 'eye_color', 'distinctive_features', 'ratio(wt/ht)', 'age'])
        data_df['age'] = pd.to_numeric(data_df['age'])
        data_df['ratio(wt/ht)'] = pd.to_numeric(data_df['ratio(wt/ht)'])
        print(data_df)
        print(data_df.dtypes)
        print(sex)
        print(eye_color)
        print(distinctive_features)
        print(height)
        print(weight)
        print(age)
        data = pd.get_dummies(data_df)
        print(data.columns)

        for col in feature_names:
            if col not in data.columns:
                data[col] = 0
            
        result = model.predict(data[feature_names])
        if result == 0:
            output_message = "Hot Hot..It's Getting Hot in Here ^_^"
        else:
            output_message = "Looks Like You Have a Good Personality :-("
        # print(output_message)
        print(data)
        print(result)
        print(feature_names)
    return render_template("index2.html", message = output_message)

if __name__ == "__main__":
    app.run(debug=True)
