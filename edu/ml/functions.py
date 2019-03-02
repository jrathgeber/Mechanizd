# -*- coding: utf-8 -*-

import numpy as np

# Easy One
def warmUpExercise():
    return(np.identity(5))

# Gradient Cost
def computeCost(X, y, theta=[[0],[0]]):
    m = y.size
    J = 0
    
    h = X.dot(theta)
    
    J = 1/(2*m)*np.sum(np.square(h-y))
    
    return(J)

# Gradient Descent
def gradientDescent(X, y, theta=[[0],[0]], alpha=0.01, num_iters=1500):
    m = y.size
    J_history = np.zeros(num_iters)
    
    for iter in np.arange(num_iters):
        h = X.dot(theta)
        theta = theta - alpha*(1/m)*(X.T.dot(h-y))
        J_history[iter] = computeCost(X, y, theta)
        return(theta, J_history)
        
        
def sigmoid(z):
    return(1 / (1 + np.exp(-z)))   