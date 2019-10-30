# -*- coding: utf-8 -*-

"""

Created on Tue Oct 29 13:25:34 2019

@author: https://github.com/numerai/example-scripts/blob/master/analysis_and_tips.ipynb

"""

import pandas
import numpy

print("Some features are predictive on their own")

df = df
eras = eras
features = features
target = "target_kazutsugi"


# The models should be scored based on the rank-correlation (spearman) with the target
def numerai_score(y_true, y_pred):
    rank_pred = y_pred.groupby(eras).apply(lambda x: x.rank(pct=True, method="first"))
    return numpy.corrcoef(y_true, rank_pred)[0,1]

# It can also be convenient while working to evaluate based on the regular (pearson) correlation
def correlation_score(y_true, y_pred):
    return numpy.corrcoef(y_true, y_pred)[0,1]


feature_scores = {
    feature: numerai_score(df[target], df[feature])
    for feature in features
}

pandas.Series(feature_scores).sort_values()

print(pandas.Series(feature_scores).sort_values())


# Single features do not work consistently though
print("Feature Strength")
by_era_correlation = pandas.Series({
    era: numpy.corrcoef(tdf[target], tdf["feature_strength34"])[0,1]
    for era, tdf in df.groupby(eras)
})
by_era_correlation.plot()

print("With a rolling 10 era average you can see some trends")
print("by_era_correlation.rolling(10).mean().plot()")
by_era_correlation.rolling(10).mean().plot()

