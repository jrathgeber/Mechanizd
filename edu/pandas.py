# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import random

# Well
first_series = pd.Series([1,2,3, np.nan ,"hello"])
print (first_series)

# Indexed
series = pd.Series([1,2,3, np.nan ,"hello"], index = ['A','B','C','Unknown','String'])
series

# Dect to pandas series
dict = {"Python": "Fun", "C++": "Outdated","Coding":"Hmm.."}
series = pd.Series(dict)
series

# Dict to pandas Series
series[['Coding','Python']]

series['Coding'] = 'Awesome'

# If it is necessary to apply any mathematical operation to Series items, you may done it like below:
num_series = pd.Series([1,2,3,4,5,6,None])
num_series_changed = num_series/2
print (num_series_changed)

# DATA FRAMES
data = {'year': [1990, 1994, 1998, 2002, 2006, 2010, 2014],
        'winner': ['Germany', 'Brazil', 'France', 'Brazil','Italy', 'Spain', 'Germany'],
        'runner-up': ['Argentina', 'Italy', 'Brazil','Germany', 'France', 'Netherlands', 'Argentina'],
        'final score': ['1-0', '0-0 (pen)', '3-0', '2-0', '1-1 (pen)', '1-0', '1-0'] }
world_cup = pd.DataFrame(data, columns=['year', 'winner', 'runner-up', 'final score'])
print(world_cup)

# Also, csv, json, txt 

# With Indexes and multiindex 
indexes = [random.randrange(0,100) for i in range(5)]
data = [{i:random.randint(0,10) for i in 'ABCDE'} for i in range(5)]
df = pd.DataFrame(data, index=[1,2,3,4,5])
print(df)