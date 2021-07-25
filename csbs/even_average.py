# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
toplam = 0
count = 0
while True:
    number = int(input("Integer? "))
    if number == 0:
        break
    if (number % 2 == 0):
        toplam += number
        count += 1
print("Average:", toplam / count)