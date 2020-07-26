# -*- coding: utf-8 -*-
"""
Spyder Editor
TRY this one with DICT
This is a temporary script file.
"""
dict_valid = {'A':'U','C':'G','G':'C','T':'A'}
outputRNA = []
validinput = True

inputDNA = input("Enter DNA String: ")

for i in inputDNA:
    if i not in dict_valid:
        print("Invalid Input")
        validinput = False
        break
    else:
        outputRNA.append(dict_valid[i])

if validinput:
    print(''.join(outputRNA))


        
