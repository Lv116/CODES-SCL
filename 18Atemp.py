#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 12:35:35 2019

@author: vyom
"""
def Series_A():
    x = eval(input("Enter desired value of x...:"))
    t= int(input("Enter the no. of terms in the series...:"))
    n=1
    s=0
    while(n<=t):
        s = s + ( x**n) / n
        n = n + 1
        print(s)
  

Series_A()
    

