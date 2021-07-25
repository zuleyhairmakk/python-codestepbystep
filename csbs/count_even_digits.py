# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def count_even_digits(digit,nums):
    count = 0
    digits = str(digit)
    for i in range(nums):
        if int(digits[i]) % 2 == 0:
               count += 1
    return count
                    



    