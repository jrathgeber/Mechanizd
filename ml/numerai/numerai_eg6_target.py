# -*- coding: utf-8 -*-


"""

Created on Tue Oct 29 15:10:30 2019

@author: https://github.com/numerai/example-scripts/blob/master/analysis_and_tips.ipynb

"""

import numpy
import pandas
import matplotlib.pyplot as plt
from sklearn import linear_model

print("Gotcha: {0, 1} are noticeably different from {0.25, 0.75}")

print("This makes training a classifier one-versus-rest behave counterintuitively.")

print("Specifically, the 0-vs-rest and 1-vs-rest classifiers seem to learn how to pick out extreme targets, and their predictions are the most correlated")


# The models should be scored based on the rank-correlation (spearman) with the target
def numerai_score(y_true, y_pred):
    rank_pred = y_pred.groupby(eras).apply(lambda x: x.rank(pct=True, method="first"))
    return numpy.corrcoef(y_true, rank_pred)[0,1]


df = df
features = [c for c in df if c.startswith("feature")]
target = "target"


# Train a standard logistic regression as a classifier
logistic = linear_model.LogisticRegression()
logistic.fit(df[features], (df[target]*4).astype(int))
logistic.score(df[features], (df[target]*4).astype(int))

# The first and last class are highly correlated
corrs=numpy.corrcoef(logistic.predict_proba(df[features]).T)
plt.imshow(corrs, vmin=-1, vmax=1, cmap="RdYlGn")
print(corrs)


# In-sample correlation is 5.4%
preds = pandas.Series(logistic.predict_proba(df[features]).dot(logistic.classes_), index=df.index)
print(numerai_score(df[target], preds))

# A standard linear model has a slightly higher correlation
linear = linear_model.LinearRegression()
linear.fit(df[features], df[target])
linear.score(df[features], df[target])

preds = pandas.Series(linear.predict(df[features]), index=df.index)

print(numerai_score(df[target], preds))

