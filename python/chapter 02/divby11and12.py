# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 2018

@author: Scott Warnock
"""

# Find a postive integer that is divisible by both 11 and 12.

def main():
    x = 1
    while True:
        if x%11 == 0 and x%12 == 0:
            break
        x = x + 1
    print(x, 'is divisible by 11 and 12.')
    
main()