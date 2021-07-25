# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def even_sum():
    x= int(input("how many integers? "))
    sum = 0
    max = 0 
    for i in range(x):
            num = int(input("next integer? "))
            if num % 2 == 0:
                 sum += num
                 if num > max:
                         max = num
    print("even sum =",sum)
    print("even max =", max)
   