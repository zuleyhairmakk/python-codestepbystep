# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def is_prime_number(n):
    factors = 0;
    for i in range(1, n + 1):
        if n % i == 0:
            factors += 1

    if factors != 2:
        return False
    else:
        return True





    