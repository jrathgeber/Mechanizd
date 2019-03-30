# -*- coding: utf-8 -*-

"""

Created on Wed Mar 27 04:57:31 2019

@author: Jason

"""

import pandas as pd
import matplotlib.pyplot as plt

from scipy.io import loadmat
from sklearn.preprocessing import StandardScaler
from scipy import linalg

pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 150)
pd.set_option('display.max_seq_items', None)

import seaborn as sns
sns.set_context('notebook')
sns.set_style('white')

data2 = loadmat('F:\ML\machine-learning-ex7\machine-learning-ex7\ex7\ex7data1.mat')
data2.keys()

X2 = data2['X']
print('X2:', X2.shape)

# Standardizing the data.
scaler = StandardScaler()
scaler.fit(X2)

U, S, V = linalg.svd(scaler.transform(X2).T)
print(U)
print(S)


plt.scatter(X2[:,0], X2[:,1], s=30, edgecolors='b',facecolors='None', linewidth=1);
# setting aspect ratio to 'equal' in order to show orthogonality of principal components in the plot
plt.gca().set_aspect('equal')
plt.quiver(scaler.mean_[0], scaler.mean_[1], U[0,0], U[0,1], scale=S[1], color='r')
plt.quiver(scaler.mean_[0], scaler.mean_[1], U[1,0], U[1,1], scale=S[0], color='r');

