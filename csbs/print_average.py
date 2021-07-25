# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def print_average():
    toplam = 0
    count = 0
    number=0
    while(True):
        number = (int(input("Type a number: ")))
        if number < 0:
            break
        toplam += number
        count += 1
        
    if toplam > 0 :
        print("Average was", (toplam / count))
                    



    