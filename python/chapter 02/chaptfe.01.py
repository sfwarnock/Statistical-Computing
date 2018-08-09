# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9, 2018

@author: scott warnock
"""

# Chapter 2 Finger Exercise 1

# Write a program that asks the user to input 10 integers, and then prints the
#   the largest odd number that was entered. If no odd number was entered, it 
#   shoule print a message to that effect.

def main():
    # get input from user and place in list
        intNums =[eval(input("Enter an integer: ")) for numbers in range(10)]
                                                                                
        odds = [oddNum for oddNum in intNums if oddNum % 2 != 0]                # evaluate if integer is even or odd.
        if odds:                                                                #find largest odd number.
            print ("Largest odd number entered is:", max(odds))
        else:                                                                   # no odd numbers entered.
            print('No odd numbers entered.')

main()        