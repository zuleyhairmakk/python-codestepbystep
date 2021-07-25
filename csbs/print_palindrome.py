# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def palindrome(x):
    x = x.casefold()
    return x == x[::-1]

def print_palindrome():
    for i in range(1):
        x = str(input("Type one or more words: "))
        ans = palindrome(x)
        
        if ans:
            print( x , "is a palindrome!")
        else:
             print( x , "is not a palindrome.")