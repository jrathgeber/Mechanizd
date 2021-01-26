# -*- coding: utf-8 -*-

import xgboost as xgb
import pandas as pd
import numpy as np


import warnings
import argparse
import os


TOURNAMENT_NAME = "nomi"
TARGET_NAME = "target"
PREDICTION_NAME = "prediction"

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
    
    
    # Get the Args which in particular have the data store path
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--data_path',
        type=str,
        help='Path to the training data'
    )
    parser.add_argument(
        '--learning_rate',
        type=float,
        default=0.001,
        help='Learning rate for SGD'
    )
    parser.add_argument(
        '--momentum',
        type=float,
        default=0.9,
        help='Momentum for SGD'
    )

    args = parser.parse_args()

    print("===== DATA =====")
    print("DATA PATH: " + args.data_path)
    print("LIST FILES IN DATA PATH...")
    print(os.listdir(args.data_path))
    print("================")
    
    
    
    print("\n Loading Numerai Data...")

    # The training data is used to train your model how to predict the targets.
    train = pd.read_csv(args.data_path + '/numerai_training_data.csv', header=0)
        
    # The tournament data is the data that Numerai uses to evaluate your model.
    tournament = pd.read_csv(args.data_path + '/numerai_tournament_data.csv', header=0)
    
    # The tournament data contains validation data, test data and live data.
    # Validation is used to test your model locally so we separate that.
    validation = tournament[tournament['data_type']=='validation']

    names = ('nomi', ) 

    for name in names:
        
        target = "target_" +  name
        submission = "F:\\Numerai\\numerai" + contest + "\\" + name + "_submission.csv"     
                
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
                      num_boost_round = 5000,  #2000
                      verbose_eval=200, 
                      #early_stopping_rounds = 1000,
                      evals=evals,
                      #feval = f1_score_cust,
                      maximize = False)
         
        # plot the important features  if desired
        #fig, ax = plt.subplots(figsize=(6,9))
        #xgb.plot_importance(xgb_model,  height=0.8, ax=ax)
        #plt.show()


        # Tuneing
        cv_results = xgb.cv(
            xgb_params,
            dtrain,
            num_boost_round=500,
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
        
        #%time
        
        # This can take some time…
        min_mae = float("Inf")
        best_params = None
        for eta in [.3, .2, .1, .05, .01, .005]:
            print("CV with eta={}".format(eta))    # We update our parameters
            xgb_params['eta'] = eta    # Run and time CV
            cv_results = xgb.cv(
                    xgb_params,
                    dtrain,
                    num_boost_round=4000,
                    seed=42,
                    nfold=5,
                    metrics=['mae'],
                    early_stopping_rounds=10
                  )    # Update best score
            mean_mae = cv_results['test-mae-mean'].min()
            boost_rounds = cv_results['test-mae-mean'].argmin()
            print("\tMAE {} for {} rounds\n".format(mean_mae, boost_rounds))
            if mean_mae < min_mae:
                min_mae = mean_mae
                best_params = eta
                print("Best params: {}, MAE: {}".format(best_params, min_mae))
                
        xgb_params['eta'] = .01






        #x_prediction = tournament[features] 
        x_prediction = xgb.DMatrix(tournament[features], feature_names = features) 
  
        preds = xgb_model.predict(x_prediction)
            
        #results = y_prediction[:, 1]
        results = preds
    
        print("Generating metrics...")

        train[PREDICTION_NAME] = xgb_model.predict(xgb.DMatrix(train[features], feature_names = features) )
        tournament[PREDICTION_NAME] = xgb_model.predict(xgb.DMatrix(tournament[features], feature_names = features) )

        # Check the per-era correlations on the training set
        train_correlations = train.groupby("era").apply(score)
    
        print(f"On training the correlation has mean {train_correlations.mean()} and std {train_correlations.std()}")
        print(f"On training the average per-era payout is {payout(train_correlations).mean()}")
        
        # Check the per-era correlations on the validation set
        validation_data = tournament[tournament.data_type == "validation"]
        validation_correlations = validation_data.groupby("era").apply(score)

        print(f"On validation the correlation has mean {validation_correlations.mean()} and std {validation_correlations.std()}")
        print(f"On validation the average per-era payout is {payout(validation_correlations).mean()}")
    
        # Create your submission
        print("")
        print("Creating submission file...")
        
        #results_df = pd.DataFrame(data={'probability_' + name:results})
        results_df = pd.DataFrame(data={'prediction':results})
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
    main(str(238))