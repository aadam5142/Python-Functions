# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 18:43:20 2020

@author: anwar
"""

#Implement a function that meets the specifications below.

#def max_val(t): 
 #   """ t, tuple or list
  #      Each element of t is either an int, a tuple, or a list
  #      No tuple or list is empty
  #      Returns the maximum int in t or (recursively) in an element of t """ 
    # Your code here
#For example,

#max_val((5, (1,2), [[1],[2]])) returns 5.
#max_val((5, (1,2), [[1],[9]])) returns 9.

def max_val(t):
    maxVal float('-inf')
    
    if isinstance(t, int):
        return t
    
    if isinstance(t, (list, tuple)):
        for x in t:
            currMax = max_value(x)
            maxval = max(maxVal, currMax)
            
    return maxVal