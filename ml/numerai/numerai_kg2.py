# -*- coding: utf-8 -*-

import xgboost as xgb
import pandas as pd
import numpy as np

from sklearn.metrics import mean_squared_error
from sklearn import metrics

import matplotlib.pyplot as plt

import warnings

import numpy


# The models should be scored based on the rank-correlation (spearman) with the target
def numerai_score(y_true, y_pred):
    rank_pred = y_pred.groupby(eras).apply(lambda x: x.rank(pct=True, method="first"))
    return numpy.corrcoef(y_true, rank_pred)[0,1]


# Somme feature enginner
# Better output

contest = str(184)

warnings.filterwarnings("ignore")
    
print("\n# Loading Numerai Data...")

# The training data is used to train your model how to predict the targets.
train = pd.read_csv('F:\\Numerai\\numerai' + contest + '\\numerai_training_data.csv', header=0)
        
# The tournament data is the data that Numerai uses to evaluate your model.
tournament = pd.read_csv('F:\\Numerai\\numerai'+ contest +'\\numerai_tournament_data.csv', header=0)
     
#train = df
   
train["erano"] = train.era.str.slice(3).astype(int)
eras = train.erano
    
    
# The tournament data is the data that Numerai uses to evaluate your model.
# tournament = pd.read_csv('F:\\Numerai\\numerai'+ contest +'\\numerai_tournament_data.csv', header=0)
    
# The tournament data contains validation data, test data and live data.
# Validation is used to test your model locally so we separate that.
validation = tournament[tournament['data_type']=='validation']
        
target = "target_kazutsugi"

train_columns = train.drop([ 'id', 'era', 'data_type'], axis=1)
    
# Transform the loaded CSV data into numpy arrays
features = [f for f in list(train_columns) if "feature" in f]
X_train = train_columns[features]
y_train = train_columns[target]
        
X_test = validation[features]
y_test = validation[target]
        
        #ids = tournament['id']
        
        # run simple xgboost classification model and check 
        # prep modeling code
        #from sklearn.model_selection import train_test_split
        #X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.3,  random_state=42)
        
xgb_params = {
            'n_jobs':2,    
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
                      num_boost_round = 100,  #2000
                      verbose_eval=50, 
                      early_stopping_rounds = 100,
                      evals=evals,
                      #feval = f1_score_cust,
                      maximize = True)
         
# plot the important features  
fig, ax = plt.subplots(figsize=(6,9))
xgb.plot_importance(xgb_model,  height=0.8, ax=ax)
plt.show()

x_prediction = xgb.DMatrix(tournament[features], feature_names = features) 
 
preds = xgb_model.predict(x_prediction)
                
print(numerai_score(train[target], pd.Series(preds)))
       
        
#results = preds
           
# Create your submission
## results_df = pd.DataFrame(data={'probability_' + name:results})
## joined = pd.DataFrame(ids).join(results_df)
## print("- joined:", joined.head())
    
# print("# Writing predictions to " + name + "_submissions.csv...")
# Save the predictions out to a CSV file.
# joined.to_csv(submission, index=False)
# Now you can upload these predictions on https://numer.ai
        


