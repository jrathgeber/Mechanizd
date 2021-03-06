# -*- coding: utf-8 -*-

"""

Created on Tue Oct 29 08:18:30 2019

@author: https://github.com/numerai/example-scripts/blob/master/analysis_and_tips.ipynb


"""


import pandas

print("The correlation can change over time")
print("You can see this by comparing feature correlations on the first half and second half on the training set")

df = df

df["erano"] = df.era.str.slice(3).astype(int)
eras = df.erano

features = [c for c in df if c.startswith("feature")]

target = "target_kazutsugi"

df1 = df[eras<=eras.median()]
df2 = df[eras>eras.median()]

corr1 = df1[features].corr().unstack()
corr1 = corr1[corr1.index.get_level_values(0) < corr1.index.get_level_values(1)]

corr2 = df2[features].corr().unstack()
corr2 = corr2[corr2.index.get_level_values(0) < corr2.index.get_level_values(1)]


# Nice
tdf = pandas.DataFrame({
    "corr1": corr1,
    "corr2": corr2,
})
tdf["corr_diff"] = tdf.corr2 - tdf.corr1
tdf.sort_values(by="corr_diff")

print(tdf)