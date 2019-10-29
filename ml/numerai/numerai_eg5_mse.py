# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 13:49:58 2019

@author: Jason
"""



df1 = df[eras<=eras.median()]
df2 = df[eras>eras.median()]

linear1 = linear_model.LinearRegression()
linear1.fit(df1[features], df1[target])
linear2 = linear_model.LinearRegression()
linear2.fit(df2[features], df2[target])

#

r2 = [
    [
        model.score(dfX[features], dfX[target])
        for dfX in [df1, df2]
    ]
    for model in [linear1, linear2]
]
print(pandas.DataFrame(r2, columns=["eval_on_1", "eval_on_2"], index=["train_on_1", "train_on_2"]))


# Note in particular that the correlation of (train_on_1, eval_on_2) is quite decent
corrs = [
    [
        numerai_score(dfX[target], pandas.Series(model.predict(dfX[features]), index=dfX.index))
        for dfX in [df1, df2]
    ]
    for model in [linear1, linear2]
]
print(pandas.DataFrame(corrs, columns=["eval_on_1", "eval_on_2"], index=["train_on_1", "train_on_2"]))

# This can be be run with XGB as well
print("XGB")
xgb1 = xgboost.XGBRegressor()
print(xgb1.fit(df1[features], df1[target]))
xgb2 = xgboost.XGBRegressor()
print(xgb2.fit(df2[features], df2[target]))

