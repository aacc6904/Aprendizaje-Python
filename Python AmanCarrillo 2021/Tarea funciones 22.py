# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 20:10:24 2021

@author: USUARIO
"""
def isYearLeap(a):
    if(a%4==0 and (a%100!=0 or a%400==0)):
        return True
    else:
        return False
    
def daysInMonth(a, m):
    if m==2:
        if isYearLeap(a)==True:
            return 29
        else:
            return 28
    if m>=1 and m<=6:
        if(m%2==0):
            return 30
        else:
            return 31
    if m>=7 and m<=12:
        if (m-6)%2==0:
            return 31
        else:
            return 30
   
testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
    yr = testYears[i]
    mo = testMonths[i]
    print(yr, mo, "->", end="")
    result = daysInMonth(yr, mo)
    if result == testResults[i]:
        print("OK")
    else:
        print("Failed")
    

