# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def class_presidents(x):
    with open(x, "r") as file:
        content = file.read().split()
        seniorVotes = []
        juniorVotes = []
        seniorNames = []
        juniorNames = []
        for i in range(0, len(content) , 3):
            if content[i+1] == "s" :
                seniorVotes.append(content[i+2])
                seniorNames.append(content[i])
            elif content[i+1] == "j" :
                juniorVotes.append(content[i+2])
                juniorNames.append(content[i])
        m = seniorVotes.index(max(seniorVotes))
        k = juniorVotes.index(max(juniorVotes))
        print(f"Sophomore Class President: {seniorNames[m]} ({max(seniorVotes)} votes)")
        print(f"Junior Class President: {juniorNames[k]} ({max(juniorVotes)} votes)")
                
                
                    



    