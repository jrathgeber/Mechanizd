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

import scipy.io #Used to load the OCTAVE *.mat files

datafile = 'F:\ML\machine-learning-ex8\machine-learning-ex8\ex8\ex8_movies.mat'
mat = scipy.io.loadmat( datafile )
Y = mat['Y']
R = mat['R']

nm, nu = Y.shape
# Y is 1682x943 containing ratings (1-5) of 1682 movies on 943 users
# a rating of 0 means the movie wasn't rated
# R is 1682x943 containing R(i,j) = 1 if user j gave a rating to movie i


#print ('Average rating for movie 1 (Toy Story): %0.2f', % \ np.mean([ Y[0][x] for x in xrange(Y.shape[1]) if R[0][x] ]))

# "Visualize the ratings matrix"
fig = plt.figure(figsize=(6,6*(1682./943.)))
dummy = plt.imshow(Y)
dummy = plt.colorbar()
dummy = plt.ylabel('Movies (%d)'%nm,fontsize=20)
dummy = plt.xlabel('Users (%d)'%nu,fontsize=20)

