# -*- coding: utf-8 -*-

# From : https://www.w3schools.com/python/python_dictionaries.asp

# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# You can access the items of a dictionary by referring to its key name, inside square brackets:

x = thisdict["model"]


# change year

thisdict["year"] = 2018
print(thisdict)


# lastly loop it
for x in thisdict:
  print(x) 
  
  
# Loop Keys ans values
for x, y in thisdict.items():
  print(x, y)   
  
  
# Values
for x in thisdict.values():
  print(x) 
  

# Bye !  
thisdict.clear()
print(thisdict)   
