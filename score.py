# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 18:47:35 2020

@author: anwar
"""

#Write a function called score that meets the specifications below.

#def score(word, f):
 #   """
  #     word, a string of length > 1 of alphabetical 
  #           characters (upper and lowercase)
   #    f, a function that takes in two int arguments and returns an int

    #   Returns the score of word as defined by the method:

    #1) Score for each letter is its location in the alphabet (a=1 ... z=26) 
     #  times its distance from start of word.  
      # Ex. the scores for the letters in 'adD' are 1*0, 4*1, and 4*2.
   # 2) The score for a word is the result of applying f to the
    #   scores of the word's two highest scoring letters. 
    #   The first parameter to f is the highest letter score, 
    #   and the second parameter is the second highest letter score.
    #   Ex. If f returns the sum of its arguments, then the 
     #      score for 'adD' is 12 
   # """
    #YOUR CODE HERE
#Paste your entire function, including the definition, in the box below. Do not leave any print statements.

def score(word, f):
    """
    word, a string of length > 1 of alphabetical
    characters (upper and lowercase)
    f, a function that takes in two int arguments and returns an int
    returns the score of word as defined by the method:
        1) Score for each letter is its location in the alphabet (a = 1 ... z = 26)
    times its distance from start of word.
    2) The score for a word is the result of applying f to the 
    scores of the word's two highest scoring letters.
    The first parameter to f is the highest letter score,
    and the second parameter is the second highest letter score.
    Ex. If f returns the sum of its arguments, then the 
        score for 'adD' is 12

    """
    
    scoreList = []
    for index in range(len(word)):
        char = word[index].upper()
        score = index * (ord(char)%64)
        scoreList.append(score)
    scoreList.sort(reverse = True)
    return f(scoreList[0], scoreList[1])