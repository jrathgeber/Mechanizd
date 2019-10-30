# -*- coding: utf-8 -*-
"""

Created on Tue Oct 29 13:25:34 2019

@author: https://github.com/numerai/example-scripts/blob/master/analysis_and_tips.ipynb

"""


# Some features are predictive on their own


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
