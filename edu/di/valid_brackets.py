# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 14:54:32 2019

@author: Not Jason


Imagine you are building a compiler. Before running any code, the compiler must check that the parentheses in the program are balanced. Every opening bracket must have a corresponding closing bracket. We can approximate this using strings. 

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. 
An input string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Note that an empty string is also considered valid.

https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-python/

"""

class Solution:
    
  # Python3 code to Check for  
  # balanced parentheses in an expression 
  
    
  def isValid(self, myString):

    open_list = ["[","{","("] 
    close_list = ["]","}",")"]        
    stack = [] 
    
    for i in myString: 
        if i in open_list: 
            stack.append(i) 
        elif i in close_list: 
            pos = close_list.index(i) 
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])): 
                stack.pop() 
            else: 
                return "Unbalanced"
    if len(stack) == 0: 
        return "Balanced"
  

# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))
