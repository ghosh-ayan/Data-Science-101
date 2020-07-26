# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 18:08:33 2020

@author: AG16979
"""


n = int(input())
ScoreList = list(map(int, input().split(' ')))
ScoreListSet = set(ScoreList)
ScoreListNoDup = list(ScoreListSet)


constraint = True
if 2<=n<=10:
    for score in ScoreList:
        if -100<=score<=100:
            pass
        else:
            constraint = False
else:
    constraint = False

if constraint:
     
    ScoreListNoDup.sort()
    RunnerUpScore = ScoreListNoDup[-2]
    print(RunnerUpScore)
    