# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 18:10:01 2021

@author: Jason
"""

__author__ = 'Tilii: https://kaggle.com/tilii7' 

import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd
from datetime import datetime
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import StratifiedKFold
from xgboost import XGBClassifier

def timer(start_time=None):
    if not start_time:
        start_time = datetime.now()
        return start_time
    elif start_time:
        thour, temp_sec = divmod((datetime.now() - start_time).total_seconds(), 3600)
        tmin, tsec = divmod(temp_sec, 60)
        print('\n Time taken: %i hours %i minutes and %s seconds.' % (thour, tmin, round(tsec, 2)))


train_df = pd.read_csv('../input/train.csv', dtype={'id': np.int32, 'target': np.int8})
Y = train_df['target'].values
X = train_df.drop(['target', 'id'], axis=1)
test_df = pd.read_csv('../input/test.csv', dtype={'id': np.int32})
test = test_df.drop(['id'], axis=1)