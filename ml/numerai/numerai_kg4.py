# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 18:10:01 2021

@author: Jason
"""


import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd
from datetime import datetime
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import StratifiedKFold
from xgboost import XGBRegressor

contest = str(247)

def timer(start_time=None):
    if not start_time:
        start_time = datetime.now()
        return start_time
    elif start_time:
        thour, temp_sec = divmod((datetime.now() - start_time).total_seconds(), 3600)
        tmin, tsec = divmod(temp_sec, 60)
        print('\n Time taken: %i hours %i minutes and %s seconds.' % (thour, tmin, round(tsec, 2)))


#train_df = pd.read_csv('input/train.csv', dtype={'id': np.int32, 'target': np.int8})
train_df = pd.read_csv('F:\\Numerai\\numerai' + contest + '\\numerai_training_data.csv', header=0)

Y = train_df['target'].values
X = train_df.drop(['target', 'id'], axis=1)


#test_df = pd.read_csv('input/test.csv', dtype={'id': np.int32})
tournament = pd.read_csv('F:\\Numerai\\numerai'+ contest +'\\numerai_tournament_data.csv', header=0)
test_df = tournament[tournament['data_type']=='validation']


#test = test_df.drop(['id'], axis=1)
test = test_df.drop(['id', 'data_type'], axis=1)


# A parameter grid for XGBoost
params = {
        'min_child_weight': [1],
        'gamma': [5],
        'subsample': [1.0],
        'colsample_bytree': [0.1],
        'max_depth': [5]
        }


#xgb = XGBClassifier(learning_rate=0.02, n_estimators=600, objective='reg:squarederror', silent=True, nthread=1)
xgb = XGBRegressor(max_depth=5, learning_rate=0.01, n_estimators=2000, n_jobs=-1, colsample_bytree=0.1)


folds = 2
param_comb = 1

skf = StratifiedKFold(n_splits=folds, shuffle = True, random_state = 1001)

random_search = RandomizedSearchCV(xgb, param_distributions=params, n_iter=param_comb, scoring='roc_auc', n_jobs=4, cv=skf.split(X,Y), verbose=3, random_state=1001 )

# Here we go
start_time = timer(None) # timing starts from this point for "start_time" variable
random_search.fit(X, Y)
timer(start_time) # timing ends here for "start_time" variable



print('\n All results:')
print(random_search.cv_results_)
print('\n Best estimator:')
print(random_search.best_estimator_)
print('\n Best normalized gini score for %d-fold search with %d parameter combinations:' % (folds, param_comb))
print(random_search.best_score_ * 2 - 1)
print('\n Best hyperparameters:')
print(random_search.best_params_)
results = pd.DataFrame(random_search.cv_results_)
results.to_csv('xgb-random-grid-search-results-01.csv', index=False)