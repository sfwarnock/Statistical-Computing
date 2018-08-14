# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 2018

@author: Scott Warnock
"""

# Write a program that ask the user to enter an interger and prints two integers,
#   root and pwr, such that 0 < pwr < 6 and root**pwr is equal to the interger entered
#   by the user. If no such pair of integers exists, it should print a message to that
#   effect.

def main():
    userInteger = eval(input('Enter an interger: '))
    ans, pwr, root = 0, 0, 0
    
    while pwr > 0 and pwr < 6:
        pwr =+ 1
        root =+ 1
        ans = root**pwr
    if ans == userInteger:
        print('The root of the integer you entered is: ', root, 'and the power is', pwr)
    else:
        print('There are no pairs of integers the form the root and power of the integer you entered.')
main()