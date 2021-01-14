# -*- coding: utf-8 -*-

"""
Created on Tue Oct 29 13:49:58 2019

@author: https://github.com/numerai/example-scripts/blob/master/analysis_and_tips.ipynb

"""


import numpy
import pandas
import xgboost

from sklearn import linear_model

# The models should be scored based on the rank-correlation (spearman) with the target
def numerai_score(y_true, y_pred):
    rank_pred = y_pred.groupby(eras).apply(lambda x: x.rank(pct=True, method="first"))
    return numpy.corrcoef(y_true, rank_pred)[0,1]

print(" Gotcha: MSE looks worse than correlation out of sample ")
print(" Models will generally be overconfident, so even if they are good are ranking rows, the Mean-Squared-Error of the residuals could be larger than event the Mean-Squared-Error of the target (r-squared<0) ")


df = df
eras = eras
features = features
target = "target"


df1 = df[eras<=eras.median()]
df2 = df[eras>eras.median()]


linear1 = linear_model.LinearRegression()
linear1.fit(df1[features], df1[target])

linear2 = linear_model.LinearRegression()
linear2.fit(df2[features], df2[target])


print("Note in particular that the R-squared of (train_on_1, eval_on_2) is slightly negative!")

r2 = [
    [
        model.score(dfX[features], dfX[target])
        for dfX in [df1, df2]
    ]
    for model in [linear1, linear2]
]
print(pandas.DataFrame(r2, columns=["eval_on_1", "eval_on_2"], index=["train_on_1", "train_on_2"]))


print("Note in particular that the correlation of (train_on_1, eval_on_2) is quite decent")
corrs = [
    [
        numerai_score(dfX[target], pandas.Series(model.predict(dfX[features]), index=dfX.index))
        for dfX in [df1, df2]
    ]
    for model in [linear1, linear2]
]
print(pandas.DataFrame(corrs, columns=["eval_on_1", "eval_on_2"], index=["train_on_1", "train_on_2"]))

# This can be be run with XGB as well
print("XGB - Eras 1st Half")
xgb1 = xgboost.XGBRegressor()
print(xgb1.fit(df1[features], df1[target]))

print("XGB - Eras 1st Half")
xgb2 = xgboost.XGBRegressor()
print(xgb2.fit(df2[features], df2[target]))

