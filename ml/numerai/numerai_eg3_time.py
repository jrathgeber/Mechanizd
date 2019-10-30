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
# contest = str(183)
# df=pandas.read_csv('F:\\Numerai\\numerai' + contest + '\\numerai_training_data.csv', header=0)

df1 = df[eras<=eras.median()]
df2 = df[eras>eras.median()]

corr1 = df1[features].corr().unstack()
corr1 = corr1[corr1.index.get_level_values(0) < corr1.index.get_level_values(1)]

corr2 = df2[features].corr().unstack()
corr2 = corr2[corr2.index.get_level_values(0) < corr2.index.get_level_values(1)]


tdf = pandas.DataFrame({
    "corr1": corr1,
    "corr2": corr2,
})
tdf["corr_diff"] = tdf.corr2 - tdf.corr1
tdf.sort_values(by="corr_diff")

print(tdf)