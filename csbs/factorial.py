# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def factorial(n):
    x=n
    if(n==0):
        x=1
    else:
        for i in range (1,n):
            x = x*i
    print(str(n) + " factorial = " + str(x))

def main ():
    factorial(4)





    