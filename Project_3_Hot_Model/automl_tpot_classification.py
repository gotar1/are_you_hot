import warnings
warnings.filterwarnings("ignore")
from sqlalchemy import create_engine
import numpy as np
import pandas as pd
import math
from tpot import TPOTClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, accuracy_score

# load dataset
engine = create_engine('sqlite:///../dataBase/Are_You_Hot.db')
hot_df = pd.read_sql('select * from hot', engine)

# Data clean up and droping columns we are not going to use to train our model.
clean_df = hot_df.drop(['name', 'dob', 'birth_year', 'height(ft)', 'weight(lbs)', 'zodiac_sign', 'hair_color', 'tattoo_body_art'], axis=1)

# some of our features are not important. so we are catogerizing them into one identifier.
clean_df['distinctive_features'] = clean_df['distinctive_features'].replace({'Bald': 'Other', 'Goatee': 'Other', 'Moles': 'Other', 'Skin': 'Other', 'Height': 'Other', 'Forehead': 'Other', 'Style': 'Other', 'Cheeks': 'Other', 'Jaw': 'Other', 'Legs': 'Other', 'Stubble': 'Other'})

# We need to convert any string/object column (categorical variables) to integer for training our model
# We use pandas get_dummies to create OneHotEncoder variables. 
cat_col = clean_df.select_dtypes(include=['object']).columns
dummies = pd.get_dummies(clean_df[cat_col],drop_first=True)
without_dummies = clean_df.drop(cat_col,axis=1)
model_data = pd.concat([dummies,without_dummies],axis=1)


# build X and y matrices
X = model_data.drop(['hot_test'], axis=1)
y = model_data[['hot_test']].values.reshape(-1)

# split to training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1, stratify=y)

# call TPOT and wait
tpot_clf = TPOTClassifier(generations=5, population_size=50, verbosity=2, n_jobs=-1,
    max_time_mins=2, scoring='f1')
tpot_clf.fit(X_train, y_train)

# evaluate result
y_hat_test = tpot_clf.predict(X_test)
print(f'F1: {f1_score(y_test, y_hat_test)}')
print(f'Acc: {accuracy_score(y_test, y_hat_test)}')

# export model into python code
tpot_clf.export('tpot_model.py')