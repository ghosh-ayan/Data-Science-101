# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 20:15:38 2020

@author: AG16979
"""
from functools import reduce


mylist = [4, 2, 3, 9, 113, 62, 34, 91]


doublelist = list(map(lambda x: x*2, mylist))
print(doublelist)

evenlist = list(filter(lambda x: x%2==0, mylist))
print(evenlist)

sumtotal = reduce(lambda x,y:x+y, mylist)
print(sumtotal)