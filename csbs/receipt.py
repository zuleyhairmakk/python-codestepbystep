# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
ef main():
    subtotal=38+40+30           # owed, assuming
    tax=subtotal*0.08   # 15% tip
    tip=subtotal*0.15
    total=subtotal+tax+tip
    print(f"Subtotal: {subtotal}")
    
    print(f"Tax: {tax}")
    print(f"Tip: {tip}")
    print(f"Total: {total}")

main()