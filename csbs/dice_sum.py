# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def digit_sum(number):
    if number<0:
        number=number*(-1)
    number=str(number)
    new=0
    for i in number:
        new +=int(i)
    return new



    