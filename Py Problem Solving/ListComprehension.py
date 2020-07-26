# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 18:26:28 2020

@author: AG16979
"""

'''
list_Squares = [x**2 for x in range(10)]
list_Cubes = [x**3 for x in range(10)]
list_poweroftwo = [2**i for i in range(1,11)]
print(list_Cubes)
print(list_Squares)
print(list_poweroftwo)
'''

mylist = [4, 2, 3, 9, 113, 62, 34, 91]
doublelist = [x*2 for x in mylist]
print(doublelist)
evenlist = [x for x in mylist if x%2==0]
print(evenlist)
sumtotal = sum([x for x in mylist])
print(sumtotal)