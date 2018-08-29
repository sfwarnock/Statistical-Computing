# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 2018

@author: Scott Warnock
"""

# finger exercise 4.0
#
# Wrtie a function isIn that accepts two stings as arguments and returns True if
#   either string occurs anywhere in the other, and False otherwise.
#   Hint: you might want to use the built-in str operation in.

def isIn(string1, string2):
    if string1 in string2:
        return True
    if string1 not in string2:
        return False