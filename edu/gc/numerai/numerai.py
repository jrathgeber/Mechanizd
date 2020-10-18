# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 14:59:51 2020

@author: Jason
"""

# [START setup]
import datetime
import os
import subprocess

from sklearn.preprocessing import LabelEncoder
import pandas as pd
from google.cloud import storage
import xgboost as xgb


# TODO: REPLACE 'BUCKET_CREATED_ABOVE' with your GCS BUCKET_ID
BUCKET_ID = 'jason_general_data'
# [END setup]


# Work out directory and create if not exists
directory = 'F:\\Numerai\\numerai' + contest + '\\'

if not os.path.exists(directory):

    # ---------------------------------------
    # 1. Add code to download the data from GCS (in this case, using the publicly hosted data).
    # AI Platform will then be able to use the data when training your model.
    # ---------------------------------------
    # [START download-data]
    census_data_filename = 'numerai_training_data.csv'

    # Public bucket holding the census data
    bucket = storage.Client().bucket('jason_general_data')

    # Path to the data inside the public bucket
    #data_dir = 'ai-platform/census/data/'
    data_dir = ''

    # Download the data
    blob = bucket.blob(''.join([data_dir, census_data_filename]))
    blob.download_to_filename(census_data_filename)
    # [END download-data]

# Numer AI stuff
print("Loading data...")
    
# The training data is used to train your model how to predict the targets.
#training_data = read_csv("numerai_training_data.csv")
# The tournament data is the data that Numerai uses to evaluate your model.
#tournament_data = read_csv("numerai_tournament_data.csv")
    
contest = str(233)
directory = 'F:\\Numerai\\numerai' + contest + '\\'

print("Loading data...")
    
# The training data is used to train your model how to predict the targets.
training_data = pd.read_csv(directory + "numerai_training_data.csv").set_index("id")

# The tournament data is the data that Numerai uses to evaluate your model.
tournament_data = pd.read_csv(directory + "numerai_tournament_data.csv").set_index("id")

#MODEL_FILE = directory + "example_model.xgb"

feature_names = [
    f for f in training_data.columns if f.startswith("feature")
]
print(f"Loaded {len(feature_names)} features")

 # This is the model that generates the included example predictions file.
 # Taking too long? Set learning_rate=0.1 and n_estimators=200 to make this run faster.
 # Remember to delete example_model.xgb if you change any of the parameters below.
model = XGBRegressor(max_depth=5, learning_rate=0.01, n_estimators=2000, n_jobs=-1, colsample_bytree=0.1)

print("Training model...")
model.fit(training_data[feature_names], training_data[TARGET_NAME])
 
print("Training model... {MODEL_FILE}")
model.save_model("F:\\Numerai\\numerai233\\example_model.xgb")