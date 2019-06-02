# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from sklearn import metrics, preprocessing, linear_model
import xgboost as xgb
from xgboost.sklearn import XGBRegressor
from xgboost.sklearn import XGBClassifier
from sklearn import  metrics

from sklearn.model_selection import GridSearchCV

#Perforing grid search
# https://github.com/anassboussarhan/xgboostnumer/blob/master/Untitled3.ipynb

import warnings
warnings.filterwarnings("ignore")

import matplotlib.pylab as plt
#%matplotlib inline
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 12, 4

# Set seed for reproducibility
np.random.seed(0)

contest=str(161)

print("# Loading data...")
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
train_bernie = train.drop(['id', 'era', 'data_type', 'target_charles', 'target_elizabeth', 'target_jordan', 'target_ken'], axis=1)

# Transform the loaded CSV data into numpy arrays
features = [f for f in list(train_bernie) if "feature" in f]
X = train_bernie[features]
Y = train_bernie['target_bernie']
x_prediction = validation[features]
ids = tournament['id']

#missing
predictors = features
target = 'target_bernie'
train = train_bernie


def modelfit(alg,useTrainCV=True, cv_folds=5, early_stopping_rounds=2):
    
    if useTrainCV:
        xgb_param = alg.get_xgb_params()
        xgtrain = xgb.DMatrix(X.values, label=Y.values)
        cvresult = xgb.cv(xgb_param, xgtrain, num_boost_round=alg.get_params()['n_estimators'], nfold=cv_folds, metrics='logloss', early_stopping_rounds=early_stopping_rounds)
        alg.set_params(n_estimators=cvresult.shape[0])
    
    #Fit the algorithm on the data
    alg.fit(X, Y,eval_metric='logloss')
        
    #Predict training set:
    dtrain_predictions = alg.predict(X)
    dtrain_predprob = alg.predict(X)
        
    #Print model report:
    print ("\nModel Report")
    print ("Accuracy : %.4g" % metrics.log_loss(Y.values, dtrain_predictions))

    feat_imp = pd.Series(alg.get_booster().get_score(importance_type='weight')).sort_values(ascending=False)   
    feat_imp.plot(kind='bar', title='Feature Importances')
    plt.ylabel('Feature Importance Score')

    
xgb1 = XGBRegressor(
 learning_rate =0.1,
 n_estimators=1000,
 max_depth=5,
 min_child_weight=1,
 gamma=0,
 subsample=0.8,
 colsample_bytree=0.8,
 objective= 'reg:linear',
 nthread=4,
 scale_pos_weight=1,
 seed=27,
 )
modelfit(xgb1)

print ("\nparam_test1")
param_test1 = {
 'max_depth':range(3,10,2),
 'min_child_weight':range(1,6,2)
}
gsearch1 = GridSearchCV(estimator = XGBRegressor( learning_rate =0.1, n_estimators=140, max_depth=5,
 min_child_weight=1, gamma=0, subsample=0.8, colsample_bytree=0.8,
 objective= 'reg:linear', nthread=2, scale_pos_weight=1, seed=27), 
 param_grid = param_test1,n_jobs=2,iid=False, cv=5, verbose=1)
gsearch1.fit(train[predictors],train[target])

print("Best Params ", gsearch1.best_params_)
print("Best Score   : %.4g" %  gsearch1.best_score_)

print ("\nparam_test2")
param_test2 = {
 'max_depth':[4,5,6],
 'min_child_weight':[4,5,6]
}
gsearch2 = GridSearchCV(estimator = XGBRegressor( learning_rate=0.1, n_estimators=140, max_depth=5,
 min_child_weight=2, gamma=0, subsample=0.8, colsample_bytree=0.8,
 objective= 'reg:linear', nthread=2, scale_pos_weight=1,seed=27), 
 param_grid = param_test2,n_jobs=2,iid=False, cv=5, verbose=1)
gsearch2.fit(train[predictors],train[target])

print("Best Params ", gsearch2.best_params_)
print("Best Score   : %.4g" %  gsearch2.best_score_)


print ("\nparam_test2b ")
param_test2b = {
 'min_child_weight':[6,8,10,12]
}

gsearch2b = GridSearchCV(estimator = XGBRegressor( learning_rate=0.1, n_estimators=140, max_depth=4,
 min_child_weight=2, gamma=0, subsample=0.8, colsample_bytree=0.8,
 objective= 'reg:linear', nthread=2, scale_pos_weight=1, seed=27), 
 param_grid = param_test2b, n_jobs=2, iid=False, cv=5, verbose=1)
gsearch2b.fit(train[predictors],train[target])

print("Best Params ", gsearch2b.best_params_)
print("Best Score   : %.4g" %  gsearch2b.best_score_)


print ("\nparam_test3")
param_test3 = {
 'gamma':[i/10.0 for i in range(0,5)]
}
gsearch3 = GridSearchCV(estimator = XGBRegressor( learning_rate =0.1, n_estimators=140, max_depth=4,
 min_child_weight=6, gamma=0, subsample=0.8, colsample_bytree=0.8,
 objective= 'reg:linear', nthread=2, scale_pos_weight=1,seed=27), 
 param_grid = param_test3,n_jobs=2,iid=False, cv=5)
gsearch3.fit(train[predictors],train[target])
print("Best Params ", gsearch3.best_params_)
print("Best Score   : %.4g" %  gsearch3.best_score_)



xgb2 = XGBRegressor(
 learning_rate =0.1,
 n_estimators=1000,
 max_depth=4,
 min_child_weight=6,
 gamma=0,
 subsample=0.8,
 colsample_bytree=0.8,
 objective= 'reg:linear',
 nthread=4,
 scale_pos_weight=1,
 seed=27)
modelfit(xgb2, train, predictors)

print ("\nparam_test4")
param_test4 = {
 'subsample':[i/10.0 for i in range(6,10)],
 'colsample_bytree':[i/10.0 for i in range(6,10)]
}
gsearch4 = GridSearchCV(estimator = XGBRegressor( learning_rate =0.1, n_estimators=177, max_depth=4,
 min_child_weight=6, gamma=0, subsample=0.8, colsample_bytree=0.8,
 objective= 'reg:linear', nthread=2, scale_pos_weight=1,seed=27), 
 param_grid = param_test4,n_jobs=2,iid=False, cv=5)
gsearch4.fit(train[predictors],train[target])
print("Best Params ", gsearch4.best_params_)
print("Best Score   : %.4g" %  gsearch4.best_score_)

print ("\nparam_test5")
param_test5 = {
 'subsample':[i/100.0 for i in range(75,90,5)],
 'colsample_bytree':[i/100.0 for i in range(75,90,5)]
}
gsearch5 = GridSearchCV(estimator = XGBRegressor( learning_rate =0.1, n_estimators=177, max_depth=4,
 min_child_weight=6, gamma=0, subsample=0.8, colsample_bytree=0.8,
 objective= 'reg:linear', nthread=2, scale_pos_weight=1,seed=27), 
 param_grid = param_test5,n_jobs=2,iid=False, cv=5)
print("Best Params ", gsearch5.best_params_)
print("Best Score   : %.4g" %  gsearch5.best_score_)

print ("\nparam_test6")
param_test6 = {
 'reg_alpha':[1e-5, 1e-2, 0.1, 1, 100]
}
gsearch6 = GridSearchCV(estimator = XGBRegressor( learning_rate =0.1, n_estimators=177, max_depth=4,
 min_child_weight=6, gamma=0.1, subsample=0.8, colsample_bytree=0.8,
 objective= 'reg:linear', nthread=2, scale_pos_weight=1,seed=27), 
 param_grid = param_test6,n_jobs=2,iid=False, cv=5)
gsearch6.fit(train[predictors],train[target])
print("Best Params ", gsearch6.best_params_)
print("Best Score   : %.4g" %  gsearch6.best_score_)

print ("\nparam_test7")
param_test7 = {
 'reg_alpha':[0, 0.001, 0.005, 0.01, 0.05]
}
gsearch7 = GridSearchCV(estimator = XGBRegressor( learning_rate =0.1, n_estimators=177, max_depth=4,
 min_child_weight=6, gamma=0.1, subsample=0.8, colsample_bytree=0.8,
 objective= 'reg:linear', nthread=2, scale_pos_weight=1,seed=27), 
 param_grid = param_test7,n_jobs=2,iid=False, cv=5)
gsearch7.fit(train[predictors],train[target])
print("Best Params ", gsearch7.best_params_)
print("Best Score   : %.4g" %  gsearch7.best_score_)

xgb3 = XGBClassifier(
 learning_rate =0.1,
 n_estimators=1000,
 max_depth=4,
 min_child_weight=6,
 gamma=0,
 subsample=0.8,
 colsample_bytree=0.8,
 reg_alpha=0.005,
 objective= 'reg:linear',
 nthread=4,
 scale_pos_weight=1,
 seed=27)
modelfit(xgb3)


xgb4 = XGBClassifier(
 learning_rate =0.01,
 n_estimators=5000,
 max_depth=4,
 min_child_weight=6,
 gamma=0,
 subsample=0.8,
 colsample_bytree=0.8,
 reg_alpha=0.005,
 objective= 'reg:linear',
 nthread=4,
 scale_pos_weight=1,
 seed=27)
modelfit(xgb4)
