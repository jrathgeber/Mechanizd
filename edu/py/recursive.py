# -*- coding: utf-8 -*-

def factorial_recursion(n):  
   if n == 1:  
       return n  
   else:  
       return n*factorial_recursion(n-1)
   
    
    
num = 15
print("The factorial of ",num," is ",factorial_recursion(num))