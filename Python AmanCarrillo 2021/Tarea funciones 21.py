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
    
print("")
#datos sugeridos
testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
            yr = testData[i]
            print(yr,"->",end="")
            result = isYearLeap(yr)
            if result == testResults[i]:
                        print("OK")
            else:
                        print("Failed")
print("")
          
#Para calcular cualquier valor
        
while True: 
    print("Ingrese el año para procesar: ")
    a=int(input())   
    print("El año "+str(a)+" es ",str(isYearLeap(a)))
    print("Presione cualquier tecla para continuar o  [s] para salir: ")
    presionar=input()
    if(presionar=='s' or presionar=='S'):
        break