# -*- coding: utf-8 -*-
"""
Created on Tue May  7 09:12:14 2019

@author: SCL1
"""

def farm_thingy():
    h = int(input('Enter number of heads:'))
    l = int(input('Enter number of legs:'))

    r = abs(l-2*h)//2
    c = (h-r)

    print('No. of rabits:' , r)
    print('No. of chickens:' , c )

farm_thingy()









