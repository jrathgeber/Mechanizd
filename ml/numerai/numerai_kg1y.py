# -*- coding: utf-8 -*-

import xgboost as xgb
import pandas as pd
import numpy as np

from sklearn.metrics import mean_squared_error
from sklearn import metrics

import matplotlib.pyplot as plt

import warnings

TOURNAMENT_NAME = "kazutsugi"
TARGET_NAME = "target_kazutsugi"
PREDICTION_NAME = "prediction_kazutsugi"

BENCHMARK = 0.002
BAND = 0.04

# Submissions are scored by spearman correlation
def score(df):
   
    return np.corrcoef( df[TARGET_NAME], df[PREDICTION_NAME].rank(pct=True, method="first") )[0,1]

# The payout function
def payout(scores):
    return ((scores - BENCHMARK)/BAND).clip(lower=-1, upper=1)


def main(contest):

    warnings.filterwarnings("ignore")
    
    print("\n# Loading Numerai Data...")

    # The training data is used to train your model how to predict the targets.
    train = pd.read_csv('F:\\Numerai\\numerai' + contest + '\\numerai_training_data.csv', header=0)
        
    # The tournament data is the data that Numerai uses to evaluate your model.
    tournament = pd.read_csv('F:\\Numerai\\numerai'+ contest +'\\numerai_tournament_data.csv', header=0)
    
    # The tournament data contains validation data, test data and live data.
    # Validation is used to test your model locally so we separate that.
    validation = tournament[tournament['data_type']=='validation']

    names = ('kazutsugi', ) 

    for name in names:
        
        target = "target_" +  name
        submission = "F:\\Numerai\\numerai" + contest + "\\" + name + "_new_submission.csv"     
                
        features = [c for c in train if c.startswith("feature")]
        train["erano"] = train.era.str.slice(3).astype(int)
        eras = train.erano
        target = "target_kazutsugi"
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
        train_columns = train.drop(['id', 'data_type'], axis=1)
        
        
        train_columns['era'] = train_columns['era'].str.replace(r'\D','').astype(int)
        validation['era'] = validation['era'].str.replace(r'\D','').astype(int)
        
        tournament['era'] = tournament['era'].str.replace(r'eraX','500')
        tournament['era'] = tournament['era'].str.replace(r'\D','').astype(int)
       
        
    
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
            'max_depth': 4, 
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
                      num_boost_round = 200,  #2000
                      verbose_eval=200, 
                      early_stopping_rounds = 100,
                      evals=evals,
                      #feval = f1_score_cust,
                      maximize = False)
         
        # plot the important features  if desired
        #fig, ax = plt.subplots(figsize=(6,9))
        #xgb.plot_importance(xgb_model,  height=0.8, ax=ax)
        #plt.show()

        #x_prediction = tournament[features] 
        x_prediction = xgb.DMatrix(tournament[features], feature_names = features) 
  
        preds = xgb_model.predict(x_prediction)
            
        #results = y_prediction[:, 1]
        results = preds
    
        print("Generating predictions...")
        #train[PREDICTION_NAME] = xgb_model.predict(xgb.DMatrix(train[features], feature_names = features) )
        tournament[PREDICTION_NAME] = xgb_model.predict(xgb.DMatrix(tournament[features], feature_names = features) )

        # Check the per-era correlations on the training set
        #train_correlations = train.groupby("era").apply(score)
    
        #print(f"On training the correlation has mean {train_correlations.mean()} and std {train_correlations.std()}")
        #print(f"On training the average per-era payout is {payout(train_correlations).mean()}")
        
        print("Generating validation data...")
        # Check the per-era correlations on the validation set
        validation_data = tournament[tournament.data_type == "validation"]
        validation_correlations = validation_data.groupby("era").apply(score)

        print(f"On validation the correlation has mean {validation_correlations.mean()} and std {validation_correlations.std()}")
        print(f"On validation the average per-era payout is {payout(validation_correlations).mean()}")
    
        # Create your submission
        print("")
        print("Creating submission file...")
        
        results_df = pd.DataFrame(data={'probability_' + name:results})
        joined = pd.DataFrame(ids).join(results_df)
        
        print("")
        print("Top rows of Submission : ", joined.head())
    
        print("")
        print("Writing predictions to " + name + "_submissions.csv...")
        joined.to_csv(submission, index=False)
        
        # Now you can upload these predictions on https://numer.ai
        print("Prepare return Value")
        
        rvalue = validation_correlations.mean()
        
        return rvalue 
                

if __name__ == '__main__':
    main(str(195))