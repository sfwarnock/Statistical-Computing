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
    pwr, root = 0, 1

    while root**pwr != userInteger and pwr < 6:
        pwr += 1
        ansOne = root ** pwr
        print('Fisrt Loop', root, pwr, ansOne)

main()