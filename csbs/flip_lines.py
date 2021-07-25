# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def flip_lines(x):
    with open(x, "r") as file:
        content= file.read().splitlines()
        k = len(content)
        if len(content) % 2 ==0:
            for i in range(0,k,2):
                print((content[i+1]).upper())
                print((content[i]).lower())
            
                      
        else:
            for i in range(0,k-1,2):
                print((content[i+1]).upper())
                print((content[i]).lower())
            print((content[k-1]).upper())
            
             
                    



    