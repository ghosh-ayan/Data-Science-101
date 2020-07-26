# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 17:55:34 2020

@author: AG16979
"""
'''

S = input()
news = ''
if 0 <len(S) <= 1000:
    for letter in S:
        if letter.isupper():
            news += letter.lower()
        elif letter.islower():
            news += letter.upper()
        else:
            news += letter
    
    print(news)
'''
def swap_case(s):
    s1 = ''
    if 0 <len(s) <= 1000:
        for letter in s:
            if letter.isupper():
                s1 += letter.lower()
            elif letter.islower():
                s1 += letter.upper()
            else:
                s1 += letter       
    return s1


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)