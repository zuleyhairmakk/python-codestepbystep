# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""


    import random

def word_chain(filename, start):
    with open(filename, 'r') as file:
        while (len(start) != 0): # While length of start is zero
          ls = [] # Initialize list
          print(start) # Print word
          file.seek(0) # Reset the line read counter index to zero
          for l in file.readlines(): # Iterate through lines
            if l[0] == start[-2] and l[1] == start[-1]: # Check if the last two characters of word matches with first 2 of any words in the list
              ls = ls + [l] # Add the matching words into the list
          if len(ls) > 0: # If lenght of ls is greater than zero
            start = random.choice(ls).strip() # Select random word from the list
          else: # If no word in the list, break
               break








