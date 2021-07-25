# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def factor_count(number):
    count = 0
    for i in range(1, number + 1):
        if (number % i == 0):
            count += 1     
    return count





    