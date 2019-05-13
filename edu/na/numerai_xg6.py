# -*- coding: utf-8 -*-

import xgboost as xgb
import pandas as pd
import numpy as np

from sklearn.metrics import mean_squared_error
from sklearn import metrics

import matplotlib.pyplot as plt

import warnings

# Somme feature enginner

# Better output

def main(contest):

    warnings.filterwarnings("ignore")
    
    print("\n# Loading Numerai Sata...")

    # The training data is used to train your model how to predict the targets.
    train = pd.read_csv('F:\\Numerai\\numerai' + contest + '\\numerai_training_data.csv', header=0)
        
    # The tournament data is the data that Numerai uses to evaluate your model.
    tournament = pd.read_csv('F:\\Numerai\\numerai'+ contest +'\\numerai_tournament_data.csv', header=0)
    
    # The tournament data contains validation data, test data and live data.
    # Validation is used to test your model locally so we separate that.
    validation = tournament[tournament['data_type']=='validation']

    names = ('bernie', 'ken', 'charles', 'frank', 'hillary') 

    #names = ('bernie', ) 

    for name in names:
        
        target = "target_" +  name
        submission = "F:\\Numerai\\numerai" + contest + "\\" + name + "_new_submission.csv"        
       
        # There are five targets in the training data which you can choose to model using the features.
        # Numerai does not say what the features mean but that's fine; we can still build a model.
        # Here we select the bernie_target.
        #train_bernie = train.drop([
        #    'id', 'era', 'data_type',
        #    'target_charles', 'target_elizabeth',
        #    'target_jordan', 'target_ken'], axis=1)

        train_columns = train.drop([
            'id', 'era', 'data_type'], axis=1)
    
        # Transform the loaded CSV data into numpy arrays
        features = [f for f in list(train_columns) if "feature" in f]
        X_train = train_columns[features]
        y_train = train_columns[target]
        X_test = validation[features]
        y_test = validation[target]
        
        ids = tournament['id']
        
        # run simple xgboost classification model and check 
        # prep modeling code
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X_train, 
                                                         y_train, 
                                                         test_size=0.3, 
                                                         random_state=42)
        
        xgb_params = {
            'max_depth':3, 
            'eta':0.05, 
            'silent':0, 
            'eval_metric':'auc',
            'subsample': 0.8,
            'colsample_bytree': 0.8,
            'objective':'binary:logistic',
            'seed' : 0
        }
        
        dtrain = xgb.DMatrix(X_train[features], y_train, feature_names = features)
        dtest = xgb.DMatrix(X_test[features], y_test, feature_names = features)
        evals = [(dtrain,'train'),(dtest,'eval')]
        xgb_model = xgb.train (params = xgb_params,
                      dtrain = dtrain,
                      num_boost_round = 2000,
                      verbose_eval=50, 
                      early_stopping_rounds = 500,
                      evals=evals,
                      #feval = f1_score_cust,
                      maximize = True)
         
        # plot the important features  
        fig, ax = plt.subplots(figsize=(6,9))
        xgb.plot_importance(xgb_model,  height=0.8, ax=ax)
        plt.show()

        #x_prediction = tournament[features] 
        x_prediction = xgb.DMatrix(tournament[features], feature_names = features) 
  
        preds = xgb_model.predict(x_prediction)
            
        #results = y_prediction[:, 1]
        results = preds
    
        print("# Creating submission...")
        # Create your submission
        results_df = pd.DataFrame(data={'probability_' + name:results})
        joined = pd.DataFrame(ids).join(results_df)
        print("- joined:", joined.head())
    
        print("# Writing predictions to " + name + "_submissions.csv...")
        # Save the predictions out to a CSV file.
        joined.to_csv(submission, index=False)
        # Now you can upload these predictions on https://numer.ai
        


if __name__ == '__main__':
    main()