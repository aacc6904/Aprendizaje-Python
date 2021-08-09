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
   
def dayOfYear(a, m, d):
    if len(str(a))==4:
        if m>=1 and m<=12: 
            if d>=1 and d<=31:
               suma=0
               for i in range(1, m):
                   resultado = daysInMonth(a, i)
                   suma += resultado
               resultado = daysInMonth(a, m)
               if d >= 1 and d <= resultado:
                   return suma + d+1
            else:
                 return None
        else:
            return None
    else:
        return None
    
#None si el año no tiene 4 digitos   
#None si el mes no esta en el rango 1 a 12
#NONE si el dia no esta en el rango 1 a 31
print("El numero de dias:",dayOfYear(1987,12,31))

   



    
 
    

