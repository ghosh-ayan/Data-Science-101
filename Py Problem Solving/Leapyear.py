# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 15:54:39 2020
Mainly to test string formatting using %s,%d,%f,%.<number of digits>f
Also to create a user defined function that takes argument, returns value
Invoking that function.
@author: AG16979
"""


def is_leap(year):
    leap = False
    if(1900<=year<=10**5):
        if year % 400 == 0:
            leap = True
        elif year % 100 == 0:
            leap = False
        elif year % 4 == 0:
            leap = True
        else:
            leap = False
    
    return leap

year = int(input())
leap = is_leap(year)
print("It is %s that it is a leap year" %leap)
