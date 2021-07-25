# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def word_stats(x):
    with open(x, "r") as file:
        content= file.read().split()
        ul =["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
             "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
             ".", ",", "!", "?", "/"]
        
        s=0
        c=0
        for i in range(0,len(content)):
            x= content[i].lower()
            s+= len(content[i])
            for k in range(0,len(ul)):
                if ul[k] in content[i]:
                    c+=1
                    ul[k]= "9"
                    
        print(f"Total words    = {len(content)}")
        print(f"Average length = {s/len(content)}")
        print(f"Unique letters = {c}")

                    



    