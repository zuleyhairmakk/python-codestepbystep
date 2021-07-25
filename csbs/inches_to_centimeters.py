# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
print("This program converts feet and inches to centimeters.")
feet=int(input("Enter number of feet: "))
inches=int(input("Enter number of inches: "))
cm= ((feet*12)+inches)*2.54
print(str(feet) + " ft " +  str(inches) + " in = " + str(cm) + " cm ")