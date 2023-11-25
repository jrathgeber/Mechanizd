# -*- coding: utf-8 -*-

import numpy as np

# Identity
c = np.identity(5)
print(c)

# Dot product
a = [[1, 0], [0, 1]]
b = [[4, 1], [2, 2]]
np.dot(a, b)
print(np.dot(a,b))

##
#np.dot(a,c)

# Arrange
q = np.arange(3*4*5*6).reshape((3,4,5,6))
w = np.arange(3*4*5*6)[::-1].reshape((5,4,6,3))
np.dot(q, w)[2,3,2,1,2,2]


# Transpose
x = np.arange(4).reshape((2,2))
x

np.transpose(x)

x = np.ones((1, 2, 3))
np.transpose(x, (1, 0, 2)).shape


