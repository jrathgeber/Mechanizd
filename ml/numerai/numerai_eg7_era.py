# -*- coding: utf-8 -*-

"""
Created on Tue Oct 29 15:12:42 2019

@author: https://github.com/numerai/example-scripts/blob/master/analysis_and_tips.ipynb

"""



#Gotcha: eras are homogenous, but different from each other
#Random cross-validation will look much better than cross-validating by era
#Even for a simple linear model, taking a random shuffle reports a correlation of 4.3%, but a time series split reports a lower score of 3.4%


crossvalidators = [
    model_selection.KFold(5),
    model_selection.KFold(5, shuffle=True),
    model_selection.GroupKFold(5),
    model_selection.TimeSeriesSplit(5)
]

def correlation_score(y_true, y_pred):
    return numpy.corrcoef(y_true, y_pred)[0,1]



for cv in crossvalidators:
    print(cv)
    print(numpy.mean(
            model_selection.cross_val_score(
            linear_model.LinearRegression(),
            df[features],
            df[target],
            cv=cv,
            n_jobs=1,
            groups=eras,
            scoring=metrics.make_scorer(correlation_score, greater_is_better=True)
        )))
    print()

