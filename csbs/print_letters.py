# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def print_letters(text):
    for i in range(0, len(text)-1): 
        print(text[i] + "-" , end="")
    print(text[-1::])   # to end the line of output
                    



    