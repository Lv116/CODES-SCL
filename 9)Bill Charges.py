#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 12:01:54 2019
"""


def Bill_Charges():
    
    u = int(input("Enter units consumed-"))
    
    c = 50
    
    if u <= 100:
        b = (u*0.4)+c
        
    elif u <= 300:
        b = 40+((u-100)*0.5)+c
        
    else:
        b = 40+(200*0.5)+((u-300)*0.6)+c
        
    
    print(f'Electical charges - Rs. {b}')


Bill_Charges()