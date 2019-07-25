#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 13:14:49 2019

@author: vyom
"""

def Date():
    d=int(input('Enter Date:'))
    
    m=int(input('Enter Month:'))
    
    y=int(input('Enter Year:'))
    
    
    L=["JAN","FEB","MAR","APR","MAY", "JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
    
    print("The Date is-",d,"-",L[m],"-",y%100)

Date()

    












