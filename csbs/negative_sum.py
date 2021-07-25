# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def negative_sum(x):
    with open(x , "r") as file:
        content= file.read().split()
        s = 0
        c = 0
        for i in range(0, len(content)):
            k = int(content[i])
            s+= k
            c+=1
            if s < 0 :
                print(f"{s} after {c} steps")
                return True
        print("no negative sum")
        return False
                
                    



    