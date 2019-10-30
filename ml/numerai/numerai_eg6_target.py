# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 15:10:30 2019

@author: https://github.com/numerai/example-scripts/blob/master/analysis_and_tips.ipynb

"""



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

