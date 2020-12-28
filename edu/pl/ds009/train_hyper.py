# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 23:36:25 2020

@author: Jason
"""


import pandas as pd
import numpy as np
import scipy.optimize as opt
from sklearn import preprocessing
import os
import argparse

from azureml.core import Workspace, Dataset, Run
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report, confusion_matrix, mean_squared_error, accuracy_score
from azureml.core import Dataset


parser = argparse.ArgumentParser()
parser.add_argument('--regularization', type=float, dest='reg', default=0.01, help='regularization rate')
parser.add_argument('--penalty', type=str, dest='penalty', default='l1', help='Penalty')
args = parser.parse_args()

run = Run.get_context()
ws = run.experiment.workspace
bank_ds = Dataset.get_by_name(ws, name="Bank Dataset") # Please change the dataset name to the name you provided.
df = bank_ds.to_pandas_dataframe()

x_col=['age','job_int','education_int'] # Please change these column names to match your data
y_col=['deposit'] # Please change these column name to match your data
run.log("regularization", args.reg) # Please change this if you changed the dest variable while passing arguments
x_df = df.loc[:,x_col]
y_df = df.loc[:,y_col]
x_train, x_test, y_train, y_test = train_test_split(x_df, y_df, test_size=0.2, random_state=223)
x_df = preprocessing.StandardScaler().fit(x_df.astype(float)).transform(x_df.astype(float))
data = {
    "train":{"X": x_train, "y": y_train},        
    "test":{"X": x_test, "y": y_test}
}


print ('Train set:', x_train.shape,  y_train.shape)
print ('Test set:', x_test.shape,  y_test.shape)

LR = LogisticRegression(penalty=args.penalty, C=args.reg, random_state=42, solver='liblinear').fit(x_train,np.ravel(y_train))
ypredict = LR.predict(x_test)
ypre_prob = LR.predict_proba(x_test)

print ('Confusion Matrix :', (y_test, ypredict))

print (classification_report(y_test, ypredict))

print('Accuracy of Logistic Regression on training set: {:.2f}'.format(LR.score(x_train, y_train)))
print('Accuracy of Logistic Regression on test set: {:.2f}'.format(LR.score(x_test, y_test)))

run.log("Traning set LR",  LR.score(x_train, y_train))
run.log("Testing set LR",  LR.score(x_test, y_test))
print ('Accuracy Score :', accuracy_score(y_test, ypredict))
run.log('Accuracy', accuracy_score(y_test, ypredict))
