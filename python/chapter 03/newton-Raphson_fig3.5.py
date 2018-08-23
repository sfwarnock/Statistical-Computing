# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 2018

@author: Scott Warnock
"""

# Newton-Raphson for square root.

# Find x such that x**2 - 24 is within epsilon of 0

def main():
    epsilon = 0.01
    k = 24.0
    guess = k / 2.0
    
    while abs(guess*guess - k) >= epsilon:
        guess = guess - (((guess**2) - k)/(2*guess))
    print('Square root of', k, 'is about', guess)

main()