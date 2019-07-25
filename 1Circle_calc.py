#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 25 22:56:55 2019

@author: vyom
"""
def Circle_calc():
   #this code calculates the area and circumference of any given radius entered by the user
    r = int(input('Enter the radius of the circle-'))
    a = 3.14*r*r
    c = 2*a/r
    print('The area of the circle is- ',a,' AND The circumference of the circle is- ',c)

Circle_calc()   
    