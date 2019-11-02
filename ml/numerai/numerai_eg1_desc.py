# -*- coding: utf-8 -*-

"""

Created on Tue Oct 29 08:18:30 2019

@author: https://github.com/numerai/example-scripts/blob/master/analysis_and_tips.ipynb

"""


import pandas


# The cotest
contest = str(183)

# Read File
df=pandas.read_csv('F:\\Numerai\\numerai' + contest + '\\numerai_training_data.csv', header=0)
df.head()
print("df.shape")
print(df.shape)

# There's 310 features
features = [c for c in df if c.startswith("feature")]
df["erano"] = df.era.str.slice(3).astype(int)
eras = df.erano
target = "target_kazutsugi"
print(len(features))

# The features are grouped together into 6 types
feature_groups = {
    g: [c for c in df if c.startswith(f"feature_{g}")]
    for g in ["intelligence", "wisdom", "charisma", "dexterity", "strength", "constitution"]
}
print("feature_groups")
print(feature_groups)


print ("") # There are 120 eras numbered from 1 to 120
print ("eras.describe()")
print (eras.describe())

print ("") # The earlier eras are smaller, but generally each era is 4000-5000 rows
print ("df.groupby(eras).size().plot()")
df.groupby(eras).size().plot()

print ("") # The target is discrete and takes on 5 different values
print ("df.groupby(target).size()")
print (df.groupby(target).size())

print ("") # Feature Correlation
print ("feature_corrs = df[features].corr()")
feature_corrs = df[features].corr()
print(feature_corrs.stack().head())