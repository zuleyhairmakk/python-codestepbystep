# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
newL = []
name = input("Enter name: ")
newL.append(name)
nameset = set()
while name != "":
    name = input("Enter name: ")
    if name == "":
        break
    else:
        newL.append(name)
        nameset.add(name)
for i in nameset:
    print(f"Entry [{i}] has count {newL.count(i)}")


    