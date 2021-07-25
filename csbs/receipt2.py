# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def main():
    # Calculate total owed, assuming 8% tax / 15% tip
    meal = int(input("What was the meal cost? $"))
    subtotal=meal
    tax = subtotal * .08
    tip = subtotal * .15
    total = subtotal + tax + tip
    
    print("Subtotal:", subtotal)
    print("Tax:", tax)
    print("Tip:", tip)
    print("Total:", total)
main()