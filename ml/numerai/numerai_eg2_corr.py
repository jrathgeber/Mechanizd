# -*- coding: utf-8 -*-

"""

Created on Tue Oct 29 08:18:30 2019

@author: https://github.com/numerai/example-scripts/blob/master/analysis_and_tips.ipynb

"""

import matplotlib
import numpy
import pandas
import random
import sklearn
import xgboost
import matplotlib.pyplot as plt


from sklearn import (
    feature_extraction, feature_selection, decomposition, linear_model,
    model_selection, metrics, svm
)


# The cotest
contest = str(183)

# Read File
#df=pandas.read_csv('F:\\Numerai\\numerai' + contest + '\\numerai_training_data.csv', header=0)

print ("") #Print Shape
print("df.shape")
print(df.shape)

print ("") # Feature Correlation
print ("feature_corrs = df[features].corr()")
feature_corrs = df[features].corr()
print(feature_corrs.stack().head())

print ("") # Stack
print ("feature_corrs.stack()")
tdf = feature_corrs.stack()
tdf = tdf[tdf.index.get_level_values(0) < tdf.index.get_level_values(1)]
tdf.sort_values()
print(tdf)