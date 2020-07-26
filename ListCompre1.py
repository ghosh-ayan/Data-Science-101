# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 19:43:08 2020

@author: AG16979
"""


X = int(input())
Y = int(input())
Z = int(input())
N = int(input())

OutputList = [[i,j,k] for i in range(X+1) for j in range(Y+1) for k in range(Z+1) if (i+j+k)!=N]
print(OutputList)

