# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 2018

@author: Scott Warnock
"""

# Square an integer.

def main():
    
    x = 3
    ans = 0
    intersLeft = x
    while (intersLeft != 0):
        ans = ans + x
        intersLeft = intersLeft - 1
    print (str(x) + '*' + str(x) + ' = ' + str(ans))
 
main() 