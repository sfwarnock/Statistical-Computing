# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 2018

@author: Scott Warnock
"""

# Find the cube root of a perfect cube.

def main():
    x = eval(input('Enter an integer: '))
    ans = 0

    while ans**3 < abs(x):
        ans = ans + 1
    if ans**3 != abs(x):
        print(x, 'is not a perfect cube')
    else:
        if x < 0:
            ans = -ans
    print('Cube root of', x, 'is', ans)

main()