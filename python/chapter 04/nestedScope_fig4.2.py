# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 2018

@author: Scott Warnock
"""

#figure 4.2 Nested scopes

def f(x):
    def g():
        x = 'abc'
        print ('x =', x)
    def h():
        z = x
        print('z = ', z)
    x += 1
    print('x = ', x)
    h()
    g()
    print('x = ', x)
    return g

x = 3
z = f(x)
print('x = ', x)
print('z = ', z)
z()