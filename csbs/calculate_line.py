# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
print('This program calculates y coordinates for a line.')
m = int(input('Enter slope (m): '))
b = int(input('Enter intercept (b): '))
x = int(input('Enter x: '))
while x != -1:
    y = m * x + b
    print('f(' + str(x) + ') = ' + str(y))
    x = int(input('Enter x: '))
