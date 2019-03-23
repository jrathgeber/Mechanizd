# -*- coding: utf-8 -*-

# %load ../../../standard_import.txt
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from scipy.io import loadmat
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from scipy import linalg

pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 150)
pd.set_option('display.max_seq_items', None)
 
#%config InlineBackend.figure_formats = {'pdf',}
#%matplotlib inline

print('\n')
print('-- Ex 7 Kmeans -- ')

import seaborn as sns
sns.set_context('notebook')
sns.set_style('white')

data1 = loadmat('F:\ML\machine-learning-ex7\machine-learning-ex7\ex7\ex7data2.mat')
print(data1.keys())

X1 = data1['X']
print('X1:', X1.shape)

km1 = KMeans(3)
print(km1.fit(X1))


print('-- Plot -- ')
plt.scatter(X1[:,0], X1[:,1], s=40, c=km1.labels_, cmap=plt.cm.prism) 
plt.title('K-Means Clustering Results with K=3')
plt.scatter(km1.cluster_centers_[:,0], km1.cluster_centers_[:,1], marker='+', s=100, c='k', linewidth=2);

