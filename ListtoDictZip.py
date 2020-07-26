# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 16:31:30 2020

@author: AG16979
"""

'''
a = [1, 2, 3, 4]
b = ['A', 'B' ,'C', 'D']

Z = list(zip(a,b))
Y = dict(zip(a,b))
X = tuple(zip(a,b))
print(Z)
print(Y)
print(X)
'''

Name = []
Score = []
N = int(input())
for i in range(N):
    str1 = input().split()
    Name.append(str1[0])
    Score.append(list(map(float, str1[1:])))
    
X = dict(zip(Name,Score))

who = input()
rounded = round(sum(X[who])/len(X[who]),2)
print("{:.2f}".format(rounded))   


'''
Possibly a smarter way of taking the input :-
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
'''




