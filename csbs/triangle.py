# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def triangle(rows):
        k = rows - 1
        for i in range(0, rows):
            for j in range(0, k):
                print(end=" ")
            k = k-1
            for j in range(0, i+1):
                 print("*", end="")
            print("")
                



    