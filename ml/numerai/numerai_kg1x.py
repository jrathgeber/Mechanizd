# -*- coding: utf-8 -*-

import xgboost as xgb
import pandas as pd
import numpy as np

from sklearn.metrics import mean_squared_error
from sklearn import metrics

import matplotlib.pyplot as plt

import warnings

import operator

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


def SelectFeatures(X, y, cutoff):

    clf = xgb.XGBClassifier(n_estimators=20, base_score=0.005)
    clf.fit(X, y)

    column_importance = clf.feature_importances_
    columns = X.columns
    column_dict = dict()
    column_list = []

    for row, value in zip(columns, column_importance):
        column_dict[row] = value

    column_dict = sorted(column_dict.items(), key=operator.itemgetter(1))
    for row, value in column_dict:
        print ('Feature:', row,'| Importance:', value)
        if value > cutoff:
            list.append(column_list, row)

    return column_list

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
        
        # Feature Importance
        
        labels = pd.DataFrame(train['target_kazutsugi'].values)
        
        combined_features = []
        attributes = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]

        for attribute in attributes:
            print("\nTraining on Attribute: {}".format(attribute.capitalize()))
            feature_df = train[[col for col in train.columns if attribute in col]]
            important_cols = SelectFeatures(feature_df, labels, 0.01)
            combined_features += important_cols

        #print("Combined Features : ")
        #print(combined_features)
                        
        
        # There are five targets in the training data which you can choose to model using the features.
        # Numerai does not say what the features mean but that's fine; we can still build a model.
        # Here we select the bernie_target.
        #train_bernie = train.drop([
        #    'id', 'era', 'data_type',
        #    'target_charles', 'target_elizabeth',
        #    'target_jordan', 'target_ken'], axis=1)

        train_columns = train.drop(['id', 'data_type'], axis=1)
        # train_columns = train.drop(['id', 'era', 'data_type'], axis=1)        
        
        train_columns['era'] = train_columns['era'].str.replace(r'\D','').astype(int)
        validation['era'] = validation['era'].str.replace(r'\D','').astype(int)
        
        tournament['era'] = tournament['era'].str.replace(r'eraX','500')
        tournament['era'] = tournament['era'].str.replace(r'\D','').astype(int)
        
    
        # Transform the loaded CSV data into numpy arrays
        #features = [f for f in list(train_columns) if "feature" in f]
        features = combined_features
        
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
                      num_boost_round = 4000,  #2000
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
    

        

if __name__ == '__main__':
    main(str(186))