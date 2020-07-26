# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 15:26:00 2020

@author: AG16979
"""

def ListFunctions():
    
    n = int(input())
    Finallist = []
    commands = []

    for i in range(n):
        commands.append(input())
    
    for i in range(n):
        s = commands[i].split(' ')
        inputisinteger = isnum(s)
        
        if inputisinteger:
            if 'insert' in s:
                Finallist.insert(int(s[1]),int(s[2]))
            elif 'print' in s:
                print(Finallist)
            elif 'remove' in s:
                Finallist.remove(int(s[1]))
            elif 'append' in s:
                Finallist.append(int(s[1]))
            elif 'sort' in s:
                Finallist.sort()
            elif 'pop' in s:
                Finallist.pop()
            elif 'reverse' in s:
                Finallist.reverse()
            else:
                pass
            
def isnum(s):
    if len(s)==1:
        return True
    elif len(s) == 2:
        if s[1].isdigit():
            return True
    elif len(s) == 3:
        if s[1].isdigit() and s[2].isdigit():
            return True
    else:
        return False

def main():
    ListFunctions()

if __name__ == "__main__":
    main()
        
            
            
        