# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def is_all_vowels(s):
    vowels = 'AEIOUaeiou '
    count = 0
    for i in s:
        if(i in vowels):
            count +=1
    if(count==len(s)):
        return True
    else:
        return False
   
                    



    