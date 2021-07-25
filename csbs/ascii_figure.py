# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def ascii_figure():
    fslash = 16
    bslash = 16
    stars = 0
    for i in range(0,5):
        for j in range(0, fslash):
            print("/", end="")
        for k in range(0,stars):
            print("*", end="")
        for j in range(0,bslash):
            print("\\", end="")

        stars = 8*(i+1)
        fslash = fslash - 4
        bslash = bslash - 4
        print()

                    



    