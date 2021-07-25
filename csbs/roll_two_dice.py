# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
x= int(input("Desired sum: "))
a = 0
b = 0 
while(a+b) != x:
    b = (random.randint(1,6))
    a = (random.randint(1,6))
    print(f"{a} and {b} = {a+b}")

                    



    