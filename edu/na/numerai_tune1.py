# -*- coding: utf-8 -*-
"""
Created on Fri May 24 18:25:14 2019

@author: Jason
"""

# XGBoost on Otto dataset, Tune learning_rate
# from pandas import read_csv
import pandas as pd

from xgboost import XGBRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import LabelEncoder
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot

import warnings


def main(contest):


    warnings.filterwarnings("ignore")

    print("\n# xg 3 : Loading Numerai Data...")
    
    # The training data is used to train your model how to predict the targets.
    train = pd.read_csv('F:\\Numerai\\numerai' + contest + '\\numerai_training_data.csv', header=0)
    
    # The tournament data is the data that Numerai uses to evaluate your model.
    tournament = pd.read_csv('F:\\Numerai\\numerai' + contest + '\\numerai_tournament_data.csv', header=0)

    # The tournament data contains validation data, test data and live data.
    # Validation is used to test your model locally so we separate that.
    validation = tournament[tournament['data_type']=='validation']

    # There are five targets in the training data which you can choose to model using the features.
    # Numerai does not say what the features mean but that's fine; we can still build a model.
    # Here we select the bernie_target.
    train_bernie = train.drop([
        'id', 'era', 'data_type',
        'target_charles', 'target_elizabeth',
        'target_jordan', 'target_ken'], axis=1)

    # Transform the loaded CSV data into numpy arrays
    features = [f for f in list(train_bernie) if "feature" in f]
    X_train = train_bernie[features]
    y_train = train_bernie['target_bernie']
    X_test = validation[features]
    y_test = validation['target_bernie']
    
    #ids = tournament['id']

    
    # grid search
    model = XGBRegressor()
    # learning_rate = [0.0001, 0.001, 0.01, 0.1, 0.2, 0.3]
    learning_rate = [0.01, 0.1]    
    param_grid = dict(learning_rate=learning_rate)
    kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=7)
    grid_search = GridSearchCV(model, param_grid, scoring="neg_log_loss", n_jobs=-1, cv=kfold)
    grid_result = grid_search.fit(X_train, y_train)
       
        
    # summarize results
    print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_))
    means = grid_result.cv_results_['mean_test_score']
    stds = grid_result.cv_results_['std_test_score']
    params = grid_result.cv_results_['params']
    for mean, stdev, param in zip(means, stds, params):
    	print("%f (%f) with: %r" % (mean, stdev, param))
    # plot
    pyplot.errorbar(learning_rate, means, yerr=stds)
    pyplot.title("XGBoost learning_rate vs Log Loss")
    pyplot.xlabel('learning_rate')
    pyplot.ylabel('Log Loss')
    pyplot.savefig('learning_rate.png')



if __name__ == '__main__':
    main(str(161))
