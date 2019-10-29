import matplotlib
import numpy
import pandas
import random
import sklearn
import xgboost
import matplotlib.pyplot as plt


from sklearn import (
    feature_extraction, feature_selection, decomposition, linear_model,
    model_selection, metrics, svm
)

#pandas.options.display.max_rows=1000
#pandas.options.display.max_columns=300

contest = str(183)

df=pandas.read_csv('F:\\Numerai\\numerai' + contest + '\\numerai_training_data.csv', header=0)
df.head()
print(df.shape)


# There's 310 features
features = [c for c in df if c.startswith("feature")]
df["erano"] = df.era.str.slice(3).astype(int)
eras = df.erano
target = "target_kazutsugi"
print(len(features))

