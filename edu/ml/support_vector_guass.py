# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

import support_vector_func as svf

from scipy.io import loadmat
from sklearn.svm import SVC

import seaborn as sns
sns.set_context('notebook')
sns.set_style('white')


# Example 2
data2 = loadmat('F:\ML\machine-learning-ex6\machine-learning-ex6\ex6\ex6data2.mat')
data2.keys()

x1 = np.array([1, 2, 1])
x2 = np.array([0, 4, -1])
sigma = 2

svf.gaussianKernel(x1, x2, sigma)

y2 = data2['y']
X2 = data2['X']

print('X2:', X2.shape)
print('y2:', y2.shape)

svf.plotData(X2, y2)

clf2 = SVC(C=50, kernel='rbf', gamma=6)
clf2.fit(X2, y2.ravel())
svf.plot_svc(clf2, X2, y2)



#Example 3
data3 = loadmat('F:\ML\machine-learning-ex6\machine-learning-ex6\ex6\ex6data3.mat')
data3.keys()


y3 = data3['y']
X3 = data3['X']

print('X3:', X3.shape)
print('y3:', y3.shape)

svf.plotData(X3, y3)

clf3 = SVC(C=1.0, kernel='poly', degree=3, gamma=10)
clf3.fit(X3, y3.ravel())
svf.plot_svc(clf3, X3, y3)

