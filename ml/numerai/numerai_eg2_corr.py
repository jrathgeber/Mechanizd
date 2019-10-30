# -*- coding: utf-8 -*-

"""

Created on Tue Oct 29 08:18:30 2019

@author: https://github.com/numerai/example-scripts/blob/master/analysis_and_tips.ipynb

"""


print("Some of the features are very correlated")
print("Especially within feature groups")

df = df
features = [c for c in df if c.startswith("feature")]

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