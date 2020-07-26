# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 15:23:22 2020
Given a list of lists, each sublist being student names and their scores,
Find all students with 2nd Lowest score
@author: AG16979
"""
# Accept the nested list as input and populate it
N = int(input())
st = []

for i in range(N):
    name = input()
    score = float(input())
    st.append([name,score])
    
# Sort the nested list, first on basis of score (ascending) and then name
# (also ascending). We can use sort() method or sorted() function. In either
# case we have to pass a lambda function as key to sort()/sorted().
# Note you can concatenate keys and use +- signs to denote asc/dsc sortkey

st.sort(key = lambda x:(x[1],x[0]))

# Below part is print only the student names with 2nd lowest score
count = 0
for i in range(N-1):
    if count > 1:
        break
    
    if st[i+1][1] > st[i][1]:
        count += 1
        if count == 1:
            print(st[i+1][0])
    else:
        if count == 1:
            print(st[i+1][0])
        
        
        

        



            
            
        
        
    
    

