# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def most_common(x):
    with open(x, "r")as file:
        content= file.read().split()
        return (max(set(content), key= content.count))

                    



    