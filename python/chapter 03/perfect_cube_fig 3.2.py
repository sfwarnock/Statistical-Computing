# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 2018

@author: Scott Warnock
"""

# Find the cube of a perfect root.

def main():
    x = eval(input('Enter an integer: '))

    for ans in range(0, abs(x) + 1):
        if ans ** 3 >= abs(x):
            break

    if ans ** 3 != abs(x):
        print(x, 'is not a perfect cube.')
    else:
        if x < 0:
            ans =- ans
        print('Cube root of', x, 'is', ans)

main()