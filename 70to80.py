# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 22:48:01 2020
Write a program to print 70 to 80, without using any numerical characters in program
and without taking any user input
@author: AG16979
"""


a,b = len("abcdefghijk"),len("abcdefghi")
for i in range(a):
    print(b * b - a + i)