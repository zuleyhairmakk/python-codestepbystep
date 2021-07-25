# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def contains(num1,num2):
        r=False
        t=0
        for i in range (len(num1)):
            for x in range (len(num2)):
                if not len(num1)-1<i+x:
                    if num1[i+x] == num2[x]:
                        
                        t=t+1
                        
                    else:
                        t=0
                    if t== len(num2):
                        r=True
                        break
        return r
                

    