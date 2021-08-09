# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 20:10:24 2021

@author: USUARIO
"""

def l100kmtompg(litros):
    G=3.785*(1/litros*100)/1.609
    return G

def mpgtol100km(galones):
    L= 100/((galones * 1.609)/3.785)
    return L

#Datos sugeridos
print("")
print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))
print("")

#Para calcular cualquier valor

while True:
    print("Presione 1 para realizar la conversion lt/km a gl/millas: ")
    print("Presione 2 para realizar la conversion gl/millas a lt/km: ")
    presionar=input()
    if(presionar=='1'):
        print("Ingrese la cantidad en litros: ")
        lt=float(input())
        print("La conversion de "+str(lt)+" lt/km es:",l100kmtompg(lt),"gl/millas")
    if(presionar=='2'):
        print("Ingrese la cantidad de galones: ")
        gl=float(input())
        print("La conversion de "+str(gl)+" gl/millas es:",mpgtol100km(gl),"lt/km")
    print("Presione cualquier tecla para continuar o  [s] para salir: ")
    presionar=input()
    if(presionar=='s' or presionar=='S'):
        break
    

     
      
        
    
    