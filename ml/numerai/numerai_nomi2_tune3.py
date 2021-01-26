# -*- coding: utf-8 -*-

import xgboost as xgb
import pandas as pd
import numpy as np

from sklearn.metrics import mean_squared_error
from sklearn import metrics

import matplotlib.pyplot as plt

import warnings

TOURNAMENT_NAME = "nomi"
TARGET_NAME = "target"
PREDICTION_NAME = "prediction"

BENCHMARK = 0.002
BAND = 0.04

warnings.filterwarnings("ignore")

print("\n RE using Numerai Data...")

# The training data is used to train your model how to predict the targets.
train = train

# The tournament data is the data that Numerai uses to evaluate your model.
tournament = tournament

# The tournament data contains validation data, test data and live data.
# Validation is used to test your model locally so we separate that.
validation = tournament[tournament['data_type']=='validation']

names = ('nomi', )

for name in names:

    target = "target_" +  name

    features = [c for c in train if c.startswith("feature")]
    train["erano"] = train.era.str.slice(3).astype(int)
    eras = train.erano
    target = "target"
    print("Len Features : " + str(len(features)))

    print ("") # There are 120 eras numbered from 1 to 120
    print ("", "eras.describe()")
    print (eras.describe())
    print ("")


    # There are five targets in the training data which you can choose to model using the features.
    # Numerai does not say what the features mean but that's fine; we can still build a model.
    # Here we select the bernie_target.
    #train_bernie = train.drop([
    #    'id', 'era', 'data_type',
    #    'target_charles', 'target_elizabeth',
    #    'target_jordan', 'target_ken'], axis=1)

    # train_columns = train.drop(['id', 'era', 'data_type'], axis=1)
    train_columns = train_columns


    #train_columns['era'] = train_columns['era'].str.replace(r'\D','').astype(int)
    #validation['era'] = validation['era'].str.replace(r'\D','').astype(int)

    #tournament['era'] = tournament['era'].str.replace(r'eraX','500')
    #tournament['era'] = tournament['era'].str.replace(r'\D','').astype(int)



    # Transform the loaded CSV data into numpy arrays
    features = [f for f in list(train_columns) if "feature" in f]
    X_train = train_columns[features]
    y_train = train_columns[target]
    X_test = validation[features]
    y_test = validation[target]

    ids = tournament['id']

    # run simple xgboost classification model and check
    # prep modeling code
    #from sklearn.model_selection import train_test_split
    #X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.3,  random_state=42)

    xgb_params = {
        'nthread': 2,
        'max_depth': 5,
        'learning_rate':0.01,
        'eval_metric':'rmse',
        #'subsample': 0.8,
        'colsample_bytree': 0.1,
        'objective':'reg:squarederror',
        #'seed' : 0
    }

    dtrain = xgb.DMatrix(X_train[features], y_train, feature_names = features)
    dtest = xgb.DMatrix(X_test[features], y_test, feature_names = features)
    evals = [(dtrain,'train'),(dtest,'eval')]

    xgb_model = xgb.train (params = xgb_params,
                  dtrain = dtrain,
                  num_boost_round = 400,  #2000
                  verbose_eval=200,
                  #early_stopping_rounds = 1000,
                  evals=evals,
                  #feval = f1_score_cust,
                  maximize = False)

    # plot the important features  if desired
    #fig, ax = plt.subplots(figsize=(6,9))
    #xgb.plot_importance(xgb_model,  height=0.8, ax=ax)
    #plt.show()


    cv_results = xgb.cv(
        xgb_params,
        dtrain,
        num_boost_round=400,
        seed=42,
        nfold=5,
        metrics={'mae'},
        early_stopping_rounds=10
    )


    print("CV Results")
    print(cv_results)


    print("CV Results Min")
    print(cv_results['test-mae-mean'].min())


    # You can try wider intervals with a larger step between
    # each value and then narrow it down. Here after several
    # iteration I found that the optimal value was in the
    # following ranges.
    
    gridsearch_params = [
            (subsample, colsample)
            for subsample in [i/10. for i in range(7,11)]
            for colsample in [i/10. for i in range(7,11)]
            ]
    
    min_mae = float("Inf")
    best_params = None# We start by the largest values and go down to the smallest
    for subsample, colsample in reversed(gridsearch_params):
        print("CV with subsample={}, colsample={}".format(
                                 subsample,
                                 colsample))    # We update our parameters
        xgb_params['subsample'] = subsample
        xgb_params['colsample_bytree'] = colsample    # Run CV
        cv_results = xgb.cv(
            xgb_params,
            dtrain,
            num_boost_round=4000,
            seed=42,
            nfold=5,
            metrics={'mae'},
            early_stopping_rounds=10
        )    # Update best score
        mean_mae = cv_results['test-mae-mean'].min()
        boost_rounds = cv_results['test-mae-mean'].argmin()
        print("\tMAE {} for {} rounds".format(mean_mae, boost_rounds))
        if mean_mae < min_mae:
            min_mae = mean_mae
            best_params = (subsample,colsample)
            print("Best params: {}, {}, MAE: {}".format(best_params[0], best_params[1], min_mae))
            
    xgb_params['subsample'] = .8
    xgb_params['colsample_bytree'] = 1.

