# -*- coding: utf-8 -*-

# From https://www.quantinsti.com/blog/decision-tree

import quandl
import talib as ta
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

df = quandl.get("CHRIS/CME_ES2")
df.head()
df.tail()
df.shape

# need to find ta ta lib
# import talib as ta
df['EMA10'] = ta.EMA(df['Settle'].values, timeperiod=10)
df['EMA30'] = ta.EMA(df['Settle'].values, timeperiod=30)
df['ATR'] = ta.ATR(df['High'].values, df['Low'].values, df['Settle'].values, timeperiod=14)
df['ADX'] = ta.ADX(df['High'].values, df['Low'].values, df['Settle'].values, timeperiod=14)
df['RSI'] = ta.RSI(df['Settle'].values, timeperiod=14)
macd, macdsignal, macdhist = ta.MACD(df['Settle'].values, fastperiod=12, slowperiod=26, signalperiod=9)
df['MACD'] = macd
df['MACDsignal'] = macdsignal
df.tail()

# Calc Predictors
# import numpy as np
df['ClgtEMA10'] = np.where(df['Settle'] > df['EMA10'], 1, -1)
df['EMA10gtEMA30'] = np.where(df['EMA10'] > df['EMA30'], 1, -1)
df['MACDSIGgtMACD'] = np.where(df['MACDsignal'] > df['MACD'], 1, -1)
df.tail()

# Targets
df['Return'] = df['Settle'].pct_change(1).shift(-1)
df['target_cls'] = np.where(df.Return > 0, 1, 0)
df['target_rgs'] = df['Return']
df.tail()

df.dropna(inplace=True)

# Create data set
predictors_list = ['ATR', 'ADX','RSI', 'ClgtEMA10', 'EMA10gtEMA30', 'MACDSIGgtMACD']
X = df[predictors_list]
X.tail()

# Select it
y_cls = df.target_cls
y_cls.tail()

# Voila
y_rgs = df.target_rgs
y_rgs.tail()

# Split data : Sk learn TY
# from sklearn.model_selection import train_test_split
y=y_cls
X_cls_train, X_cls_test, y_cls_train, y_cls_test = train_test_split(X, y, test_size=0.3, random_state=432, stratify=y)

print (X_cls_train.shape, y_cls_train.shape)
print (X_cls_test.shape, y_cls_test.shape)

# Regression
train_length = int(len(df)*0.70)
X_rgs_train = X[:train_length]
X_rgs_test = X[train_length:]
y_rgs_train = y_rgs[:train_length]
y_rgs_test = y_rgs[train_length:]

print (X_rgs_train.shape, y_rgs_train.shape)
print (X_rgs_test.shape, y_rgs_test.shape)

#from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(criterion='gini', max_depth=3, min_samples_leaf=6)
clf

clf = clf.fit(X_cls_train, y_cls_train)
clf

# Visualize Decision Trees for Classification

from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO  
from IPython.display import Image  
import pydotplus
   
dot_data2 = StringIO()

export_graphviz(clf, out_file=dot_data2, filled=True, rounded=True, special_characters=True,feature_names = predictors_list)
graph = pydotplus.graph_from_dot_data(dot_data2.getvalue())  
graph.write_png('tree1.png')
Image(graph.create_png())


#Make forecast
#Now let’s make predictions with data sets reserved for testing, this is the part that will let us know if the algorithm is reliable with unknown data in training.

y_cls_pred = clf.predict(X_cls_test)

from sklearn.metrics import classification_report
report = classification_report(y_cls_test, y_cls_pred)
print(report)

# Regression tree model
from sklearn.tree import DecisionTreeRegressor
dtr = DecisionTreeRegressor(min_samples_leaf = 200)
dtr.fit(X_rgs_train, y_rgs_train)
dot_data = StringIO()
export_graphviz(dtr,
                  out_file=dot_data,
                  filled=True,
                  feature_names=predictors_list)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('tree2.png')
Image(graph.create_png())
