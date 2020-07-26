# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 16:06:41 2020

Input has to be taken as an integer.
Sample Input: 3
Sample Output: 123
Sample Input: 5
Sample Output: 12345
    n = int(input())
    i = 1
    while i <= n:
        print(i, end = '')
        i+=1

Teaches:-
1. Nested functions and methods
2. Introduces Map function to apply a function to an iterable and then casting 
that iterbale to a list and then printing that list as a string
3. Also demonstrates that join() function can only join a list of strings, so
map() function is required to convert list of integers using list(range()) to 
a list of strings
4. Shows (Start,Stop) format of range function
@author: AG16979
"""


#n = (int(input()))
print(''.join(list(map(str, list(range(1,(int(input()))+1))))))
"""
    print(''.join(y)) ---> Does not work here. join() fucntion takes only a 
                           list of strings. It will not take a list of integers
"""