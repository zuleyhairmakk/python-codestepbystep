# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
import random
a = random.randint(0,10)
print("Welcome to Piglet!")
print(f"You rolled a {a}")
if a == 1:
    print("You got 0 points.")
total = a
while True:
    b = random.randint(0,10)
    answ = input("Roll again? ")
    if answ == "yes" or answ== "y":
        print(f"You rolled a {b}")
        total+=b
        if b ==1:
            print("You got 0 points.")
            break
    else:
        print(f"You got {total} points.")
        break
        

                    



    