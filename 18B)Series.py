#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 13:05:45 2019

@author: vyom
"""
import math
def Series_B():
    n = int(input("Enter desired value of n..:-"))
    m=0
    s=0
    while(m<=n):
        s = s + m/math.sqrt(m+1)
        m = m + 1
    print(s)
  

Series_B()
    

