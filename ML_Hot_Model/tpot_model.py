import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectPercentile, f_classif
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.pipeline import make_pipeline, make_union
from tpot.builtins import StackingEstimator

engine = create_engine('sqlite:///../dataBase/Are_You_Hot.db')
clean_df = pd.read_sql('select * from hot', engine)

# Data clean up and droping columns we are not going to use to train our model.
clean_df = hot_df.drop(['name', 'dob', 'birth_year', 'height(ft)', 'weight(lbs)', 'zodiac_sign', 'hair_color', 'tattoo_body_art'], axis=1)

# some of our features are not important. so we are catogerizing them into one identifier.
clean_df['distinctive_features'] = clean_df['distinctive_features'].replace({'Bald': 'Other', 'Goatee': 'Other', 'Moles': 'Other', 'Skin': 'Other', 'Height': 'Other', 'Forehead': 'Other', 'Style': 'Other', 'Cheeks': 'Other', 'Jaw': 'Other', 'Legs': 'Other', 'Stubble': 'Other'})

# We need to convert any string/object column (categorical variables) to integer for training our model
# We use pandas get_dummies to create OneHotEncoder variables. 
cat_col = clean_df.select_dtypes(include=['object']).columns
dummies = pd.get_dummies(clean_df[cat_col],drop_first=True)
without_dummies = clean_df.drop(cat_col,axis=1)
tpot_data = pd.concat([dummies,without_dummies],axis=1)

# NOTE: Make sure that the outcome column is labeled 'hot_test' in the data file
features = tpot_data.drop('hot_test', axis=1)
training_features, testing_features, training_target, testing_target = \
            train_test_split(features, tpot_data['hot_test'], random_state=None)

# Average CV score on the training set was: 0.5245645871452324
exported_pipeline = make_pipeline(
    StackingEstimator(estimator=MultinomialNB(alpha=10.0, fit_prior=True)),
    StackingEstimator(estimator=RandomForestClassifier(bootstrap=True, criterion="entropy", max_features=0.5, min_samples_leaf=12, min_samples_split=2, n_estimators=100)),
    SelectPercentile(score_func=f_classif, percentile=74),
    GaussianNB()
)

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)
