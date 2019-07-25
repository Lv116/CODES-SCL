#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 04:01:21 2019

@author: vyom
"""

n_1 = int(input("Enter the no."))
n_2 = n_1

s_odd=0
m_even=1


while (n_1>0):
    s_odd= s_odd + n_1%10
    n_1 = n_1//100

while (n_2>1):
    n_2 = n_2//10
    m_even = m_even * (n_2%10)
    n_2 = n_2//10

print ("The sum of odd digits is=",s_odd)  
print ("Product of even digit is=",m_even)

