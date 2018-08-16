# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 2018

@author: Scott Warnock
"""

# Let s be a string that contains a sequence of decimal numbers separated bu commas,
#   e.g., s = '1.23, 1.4, 3.123'. Wrtie a program that prints the sum of the numbers in s.

def main():
    
    userNumbers = eval(input('Enter a sequence of seprated by a comma: '))
    total = sum(userNumbers) 
    
    print(total)
    
main()  