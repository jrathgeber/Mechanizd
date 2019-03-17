# -*- coding: utf-8 -*-

# %load ../../../standard_import.txt

from scipy.io import loadmat
from sklearn.svm import SVC

import support_vector_func as svf 

import seaborn as sns
sns.set_context('notebook')
sns.set_style('white')
    
data1 = loadmat('F:\ML\machine-learning-ex6\machine-learning-ex6\ex6\ex6data1.mat')
data1.keys()

y1 = data1['y']
X1 = data1['X']

print('X1:', X1.shape)
print('y1:', y1.shape)

svf.plotData(X1,y1)

#SVM1
clf = SVC(C=1.0, kernel='linear')
clf.fit(X1, y1.ravel())
svf.plot_svc(clf, X1, y1)

#SVM2
clf.set_params(C=100)
clf.fit(X1, y1.ravel())
svf.plot_svc(clf, X1, y1)