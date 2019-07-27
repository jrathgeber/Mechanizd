# -*- coding: utf-8 -*-

import xgboost as xgb
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np


def main(contest):


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
    
   
    # Need Xg Boot here
    xg_reg = xgb.XGBRegressor(objective ='reg:linear', colsample_bytree = 0.3, learning_rate = 0.1, max_depth = 5, alpha = 10, n_estimators = 10)
    xg_reg.fit(X_train,y_train)
    preds = xg_reg.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, preds))
    print("RMSE: %f" % (rmse))

    # SG Boost Needs This
    data_dmatrix = xgb.DMatrix(data=X_train,label=y_train)

    # K-fold cross validation
    params = {"objective":"reg:linear",'colsample_bytree': 0.3,'learning_rate': 0.1, 'max_depth': 5, 'alpha': 10}
    cv_results = xgb.cv(dtrain=data_dmatrix, params=params, nfold=3, num_boost_round=50,early_stopping_rounds=10,metrics="rmse", as_pandas=True, seed=123)
    cv_results.head()
    print((cv_results["test-rmse-mean"]).tail(1))
    
    # Plotting
    import matplotlib.pyplot as plt
    
    import os
    os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
    
    xg_reg = xgb.train(params=params, dtrain=data_dmatrix, num_boost_round=10)
    xgb.plot_tree(xg_reg,num_trees=0)
    plt.rcParams['figure.figsize'] = [50, 10]
    plt.show()
    
    # Feature importnance
    xgb.plot_importance(xg_reg)
    plt.rcParams['figure.figsize'] = [5, 5]
    plt.show()


if __name__ == '__main__':
    main(str(161))

