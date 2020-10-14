# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 14:45:13 2020

@author: Jason
"""





# -*- coding: utf-8 -*-

#!/usr/bin/env python
"""
Example classifier on Numerai data using a xgboost regression.
To get started, install the required packages: pip install pandas numpy sklearn xgboost
"""

import csv
from pathlib import Path

import pandas as pd
import numpy as np
from xgboost import XGBRegressor

TOURNAMENT_NAME = "kazutsugi"
TARGET_NAME = f"target_{TOURNAMENT_NAME}"
PREDICTION_NAME = f"prediction_{TOURNAMENT_NAME}"

MODEL_FILE = Path("F:\\Numerai\\numerai233\\example_model.xgb")


# Submissions are scored by spearman correlation
def correlation(predictions, targets):
    ranked_preds = predictions.rank(pct=True, method="first")
    return np.corrcoef(ranked_preds, targets)[0, 1]


# convenience method for scoring
def score(df):
    return correlation(df[PREDICTION_NAME], df[TARGET_NAME])


# Payout is just the score cliped at +/-25%
def payout(scores):
    return scores.clip(lower=-0.25, upper=0.25)


# Read the csv file into a pandas Dataframe as float16 to save space
def read_csv(file_path):
    with open(file_path, 'r') as f:
        column_names = next(csv.reader(f))

    dtypes = {x: np.float16 for x in column_names if x.startswith(('feature', 'target'))}
    df = pd.read_csv(file_path, dtype=dtypes, index_col=0)

    # Memory constrained? Try this instead (slower, but more memory efficient)
    # see https://forum.numer.ai/t/saving-memory-with-uint8-features/254
    # dtypes = {f"target_{TOURNAMENT_NAME}": np.float16}
    # to_uint8 = lambda x: np.uint8(float(x) * 4)
    # converters = {x: to_uint8 for x in column_names if x.startswith('feature')}
    # df = pd.read_csv(file_path, dtype=dtypes, converters=converters)

    return df


def main():
    
    print(MODEL_FILE)
    
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