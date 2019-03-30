# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 12:00:40 2019

@author: Jason
"""

# %load ../../../standard_import.txt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from scipy.io import loadmat
from sklearn.svm import OneClassSVM
from sklearn.covariance import EllipticEnvelope

pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 150)
pd.set_option('display.max_seq_items', None)
 
#%config InlineBackend.figure_formats = {'pdf',}
#%matplotlib inline

import seaborn as sns
sns.set_context('notebook')
sns.set_style('white')

data2 = loadmat('F:\ML\machine-learning-ex8\machine-learning-ex8\ex8\ex8_movies.mat')
data2.keys()

Y = data2['Y']
R = data2['R']
print('Y:', Y.shape)
print('R:', R.shape)

Y

R

sns.heatmap(Y, yticklabels=False, xticklabels=False);