# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 13:28:52 2020
Enter a dot separated string. program should return a string with all the 
individual dot separated words reversed
Sample Input: mom.is.so.good
Sample Output: mom.si.os.doog

1)Split is necessary to get a list having individual words
2)loop should run on index (not as an item in list, as each item value is a copy
of each element in list,changing the copy does not change the list itself)
,indexed loops give access to directly modify the list items in place. 
3)Resultant modified list can be joined back into a string with dot separator
by using join() function by giving '.' as separator to link the list elements
into a single string separated by dots.
@author: AG16979
"""
"""
splt = input().split('.')
for i in range(len(splt)):    
    splt[i] = splt[i][::-1]
print('.'.join(splt))
"""
print('.'.join(list(reversed((''.join(list(reversed(input())))).split('.')))))

