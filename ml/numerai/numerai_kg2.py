# -*- coding: utf-8 -*-

import xgboost as xgb
import pandas as pd
import numpy
import warnings


TOURNAMENT_NAME = "kazutsugi"
TARGET_NAME = "target_kazutsugi"
PREDICTION_NAME = "prediction_kazutsugi"

BENCHMARK = 0.002
BAND = 0.04

# Submissions are scored by spearman correlation
def score(df):
    
    # method="first" breaks ties based on order in array
    return numpy.corrcoef( df[TARGET_NAME], df[PREDICTION_NAME].rank(pct=True, method="first") )[0,1]

# The payout function
def payout(scores):
    return ((scores - BENCHMARK)/BAND).clip(lower=-1, upper=1)


# The models should be scored based on the rank-correlation (spearman) with the target
def numerai_score(y_true, y_pred):
    rank_pred = y_pred.groupby(eras).apply(lambda x: x.rank(pct=True, method="first"))
    return numpy.corrcoef(y_true, rank_pred)[0,1]


# The Script Enter the Week Number Below

contest = str(186)
warnings.filterwarnings("ignore")
print("\n# Loading Numerai Data...")
     

# The training data is used to train your model how to predict the targets.
train = pd.read_csv('F:\\Numerai\\numerai' + contest + '\\numerai_training_data.csv', header=0)
        
# The tournament data is the data that Numerai uses to evaluate your model.
tournament = pd.read_csv('F:\\Numerai\\numerai'+ contest +'\\numerai_tournament_data.csv', header=0)
   
   
train["erano"] = train.era.str.slice(3).astype(int)
eras = train.erano
    
    
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
        
ids = tournament['id']
        
# run simple xgboost classification model and check 
# prep modeling code
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.3,  random_state=42)
        
xgb_params = {
            'nthread': 2,    
            'max_depth': 5, 
            'learning_rate': 0.01, 
            'eval_metric': 'rmse',
            #'subsample': 0.8,
            'colsample_bytree': 0.1,
            'objective':'reg:squarederror'#,
            #'seed' : 0
      }
        
dtrain = xgb.DMatrix(X_train[features], y_train, feature_names = features)
dtest = xgb.DMatrix(X_test[features], y_test, feature_names = features)
       
evals = [(dtrain,'train'),(dtest,'eval')]
        
xgb_model = xgb.train (params = xgb_params,
                      dtrain = dtrain,
                      num_boost_round = 2000,  #2000
                      verbose_eval=100, 
                      #early_stopping_rounds = 100,
                      evals=evals,
                      maximize = False)
         
# plot the important features  
# import matplotlib.pyplot as plt
# fig, ax = plt.subplots(figsize=(6,9))
# xgb.plot_importance(xgb_model,  height=0.8, ax=ax)
# plt.show()

x_prediction = xgb.DMatrix(tournament[features], feature_names = features) 
 
preds = xgb_model.predict(x_prediction)

print("Generating metrics...")
    
# training_data[PREDICTION_NAME] = model.predict(training_data[feature_names])
# tournament_data[PREDICTION_NAME] = model.predict(tournament_data[feature_names])    

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

print("Generating Submission...")
           
# Needed Vars to Gen the CSV
results = preds
name = 'kazutsugi' 
submission = "F:\\Numerai\\numerai" + contest + "\\" + name + "_Nm_Example_Submission.csv"    

# Create your submission
results_df = pd.DataFrame(data={'probability_' + name:results})
joined = pd.DataFrame(ids).join(results_df)
print("- joined:", joined.head())
    
print("# Writing predictions to " + name + "_Nm_Example_Submission.csv")
joined.to_csv(submission, index=False)

        


