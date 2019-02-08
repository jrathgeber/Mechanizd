# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 09:11:20 2019

@author: jrathgeber

https://www.quantinsti.com/blog/cross-validation-machine-learning-trading-models?utm_campaign=News&utm_medium=Community&utm_source=DataCamp.com

And

https://github.com/QuantInsti/Quantra-Courses/blob/master/quantrautil.py


"""

import quantrautil as q
import numpy as np
from sklearn import tree

aapl = q.get_data('aapl','2000-1-1','2019-1-1')
print(aapl.tail())

# Features construction 
aapl['Open-Close'] = (aapl.Open - aapl.Close)/aapl.Open
aapl['High-Low'] = (aapl.High - aapl.Low)/aapl.Low
aapl['percent_change'] = aapl['Close'].pct_change()
aapl['std_5'] = aapl['percent_change'].rolling(5).std()
aapl['ret_5'] = aapl['percent_change'].rolling(5).mean()
aapl.dropna(inplace=True)

# X is the input variable
X = aapl[['Open-Close', 'High-Low', 'std_5', 'ret_5']]

# Y is the target or output variable
y = np.where(aapl['Close'].shift(-1) > aapl['Close'], 1, -1)

clf = tree.DecisionTreeClassifier(random_state=5)
model = clf.fit(X, y)

# Then
from sklearn.metrics import accuracy_score
print('Correct Prediction: ', accuracy_score(y, model.predict(X), normalize=False))
print('Total Prediction: ', X.shape[0])

print(accuracy_score(y, model.predict(X), normalize=True)*100)

# Total dataset length
dataset_length = aapl.shape[0]

# Training dataset length
split = int(dataset_length * 0.75)
split

# Splittiing the X and y into train and test datasets
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# Print the size of the train and test dataset
print(X_train.shape, X_test.shape) 
print(y_train.shape, y_test.shape) 

# Create the model on train dataset
model = clf.fit(X_train, y_train)

# Calculate the accuracy
accuracy_score(y_test, model.predict(X_test), normalize=True)*100

# K-Fold Starts Here
from sklearn.model_selection import KFold
kf = KFold(n_splits=4,shuffle=False)

kf.split(X)

print("Train: ", "TEST:")
for train_index, test_index in kf.split(X):
     print(train_index, test_index)


# Initialize the accuracy of the models to blank list. The accuracy of each model will be appended to this list
accuracy_model = []

# Iterate over each train-test split
for train_index, test_index in kf.split(X):
    # Split train-test
    X_train, X_test = X.iloc[train_index], X.iloc[test_index]
    y_train, y_test = y[train_index], y[test_index]
    
    # Train the model
    model = clf.fit(X_train, y_train)
    
    # Append to accuracy_model the accuracy of the model
    accuracy_model.append(accuracy_score(y_test, model.predict(X_test), normalize=True)*100)
    
# Print the accuracy    
print(accuracy_model)


# Stability of the model
np.std(accuracy_model)

np.mean(accuracy_model)

# Confusion Matrix


# Import the pandas for creating a dataframe
import pandas as pd

# To calculate the confusion matrix
from sklearn.metrics import confusion_matrix

# To plot
#%matplotlib inline

import matplotlib.pyplot as plt
import seaborn as sn

# Initialize the array to zero which will store the confusion matrix
array = [[0,0],[0,0]]

# For each train-test split: train, predict and compute the confusion matrix
for train_index, test_index in kf.split(X):
    # Train test split
    X_train, X_test = X.iloc[train_index], X.iloc[test_index]
    y_train, y_test = y[train_index], y[test_index]
    
    # Train the model
    model = clf.fit(X_train, y_train)
    
    # Calculate the confusion matrix
    c = confusion_matrix(y_test, model.predict(X_test))   
    
    # Add the score to the previous confusion matrix of previous model
    array = array + c
        
# Create a pandas dataframe that stores the output of confusion matrix        
df = pd.DataFrame(array, index = ['Buy', 'Sell'], columns = ['Buy', 'Sell'])

# Plot the heatmap
sn.heatmap(df, annot=True, cmap='Greens', fmt='g')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()



