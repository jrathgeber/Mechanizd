# -*- coding: utf-8 -*-

"""
Created on Tue Oct 29 15:14:48 2019

@author: https://github.com/numerai/example-scripts/blob/master/analysis_and_tips.ipynb

"""

# The results are sensitive to the choice of parameters, which should be picked through cross-validation¶


df1 = df[eras<=eras.median()]
df2 = df[eras>eras.median()]

#

models = [
    linear_model.LinearRegression(),
] + [
    linear_model.ElasticNet(alpha=alpha)
    for alpha in [0.01, 0.005, 0.002, 0.001, 0.0005, 0.0002, 0.0001, 0.00005, 0.00002, 0.00001]
] + [
    xgboost.XGBRegressor(n_jobs=-1),
    xgboost.XGBRegressor(n_jobs=-1, learning_rate=0.01, n_estimators=1000),
    xgboost.XGBRegressor(n_jobs=-1, colsample_bytree=0.1, learning_rate=0.01, n_estimators=1000),
    xgboost.XGBRegressor(n_jobs=-1, colsample_bytree=0.1, learning_rate=0.01, n_estimators=1000, max_depth=5),
    xgboost.XGBRegressor(n_jobs=-1, colsample_bytree=0.1, learning_rate=0.001, n_estimators=10000, max_depth=5),
]


#

for model in models:
    print(" -- ", model)   
    model.fit(df1[features], df1[target])
    outsample = numerai_score(df2[target], pandas.Series(model.predict(df2[features]), index=df2.index))
    insample = numerai_score(df1[target], pandas.Series(model.predict(df1[features]), index=df1.index))
    print(
        f"outsample: {outsample}, insample: {insample}"
    )
    print()

