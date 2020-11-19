# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 17:17:26 2020

@author: anwar
"""

#Write a recursive Python function, given a non-negative integer N,
# to count and return the number of occurrences of the digit 7 in N.

#For example:
#count7(717) -> 2
#count7(1237123) -> 1
#count7(8989) -> 0
#Hint: Mod (%) by 10 gives you the rightmost digit (126 % 10 is 6),
# while doing integer division by 10 removes the rightmost digit (126 // 10 is 12).

#This function has to be recursive; you may not use loops! This function takes in one integer and returns one integer.

def count7(n):
    n = str(N)
    if not n:
        return 0
    else:
        return (n[0] == "7") + count7(n[1:])