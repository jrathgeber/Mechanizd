# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 11:14:43 2019

@author: Jason
"""

import pandas as pd
import numpy as np
from xgboost import XGBClassifier

X = np.array([[0], [0], [1]])
y = np.array([0, 0, 1])
w = pd.Series([1, 1, 1])
clf = XGBClassifier()
clf.fit(X, y, w)
