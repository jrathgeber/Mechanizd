# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 15:30:21 2019

@author: Jason

You are given a list of numbers, and a target number k. Return whether or not there are two numbers in the list that add up to k.


"""

def two_sum(list, k):
  # Fill this in.

    result = False

    for i in list:
        print(i)
        
        for j in list:
            print(j) 
        
            if i * j == k:
                result = True

    return result


print (two_sum([4,7,1,-3,2, 5], 5))

# True

