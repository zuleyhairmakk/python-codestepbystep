# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
x = str(input("Input file? "))
with open(x, "r") as file:
    content = file.read().split()
    prev = float(content[0])
    alph = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ":",
            ")"]
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    mystr= []
    mynum= []
    for i in range(1, len(content)):
        for k in range(0, len(alph)):
            if alph[k] in content[i]:
                mystr.append(content[i])
                content[i]=""
        for x in range(0, len(nums)):
            if nums[x] in content[i]:
                mynum.append(content[i])
                content[i] = ""
    for i in range(0, len(mynum)):
        s = float(mynum[i])
        d = float(s - prev)
        print(f"{prev} to {s}, change = {round(d,1)}")
        prev=s
                    



    