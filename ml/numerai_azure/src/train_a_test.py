# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 17:38:06 2020

@author: Jason
"""

# -*- coding: utf-8 -*-

import xgboost as xgb
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np

from sklearn.datasets import load_boston
boston = load_boston()

print("\n-- XG Boot --")
print(boston.keys())
print(boston.data.shape)
print(boston.feature_names)
print(boston.DESCR)

# Pandas Bit
data = pd.DataFrame(boston.data)
data.columns = boston.feature_names
data.head()
data.info()
data.describe()


# Xg Boost
X, y = data.iloc[:,:-1],data.iloc[:,-1]
data_dmatrix = xgb.DMatrix(data=X,label=y)


# Train Test Split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)
xg_reg = xgb.XGBRegressor(objective ='reg:squarederror', colsample_bytree = 0.3, learning_rate = 0.1, max_depth = 5, alpha = 10, n_estimators = 10)
xg_reg.fit(X_train,y_train)
preds = xg_reg.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, preds))
print("RMSE: %f" % (rmse))


# K-fold cross validation
params = {"objective":"reg:linear",'colsample_bytree': 0.3,'learning_rate': 0.1, 'max_depth': 5, 'alpha': 10}
cv_results = xgb.cv(dtrain=data_dmatrix, params=params, nfold=3, num_boost_round=50,early_stopping_rounds=10,metrics="rmse", as_pandas=True, seed=123)
cv_results.head()
print((cv_results["test-rmse-mean"]).tail(1))

