# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def print_pyramid(): 
    n=0
    r = 7
    for m in range(1, r):
        for gap in range(1, (r-m)+1):
            print(end=" ")
        while n != (2*m-1):
            print("*",end="")
            n = n + 1
        n = 0
        print()
                    



    