# -*- coding: utf-8 -*-

"""
Created on Fri Jun 12 13:28:52 2020
Enter a dot separated string. program should return a string with all the 
words in reversed order in full string
Sample Input: dog.is.very.nice
Sample Output: nice.very.is.dog

1)Split method is necessary to get a list having individual words from input()
function returned string
2)reversed() function takes the returned list from split() method and retruns
a reversed iterable that is cast into a list by list() function.
3)This resultant list elements can be joined back into a string with dot separator
by using join() function by giving '.' as separator to link the list elements
into a single string separated by dots.
@author: AG16979
"""

print('.'.join(list(reversed(input().split('.')))))

"""
Why can't we use reverse() method above instead of reversed() function?
x = input().split('.')
y= x.reverse()  --> This code does not work, because reverse() method does not
print(y)            return anything(returns None). It reverses list in place. 
                    For the same reason, reverse() cannot be used as a nested
                    method, because the outer method will not receive anything
                    from reverse(). In such situation if nesting is required,
                    instead of reverse() method, use reversed() function.
                    reversed() returns a reversed object interable that can
                    be converted into a list by list() function
x = input().split('.')
y =  list(reversed(x))
print(y)
                    

"""