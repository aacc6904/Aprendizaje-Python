# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 20:10:24 2021

@author: USUARIO
"""
try:
    print("Inicio")
    x=1/0
    print("Resultatdo")
except:
    print("Hay un error")
print("Fin")


try:
    x=int(input("Enter a number:"))
    y=1/x
    print(y)
except ZeroDivisionError:
    print("Division para cero")
except ValueError:
    print("Ingrese un entero")
except:
    print("Error en la division")
print("Fin")


try:
    y=1/0
except ZeroDivisionError:
    print("Error Aritmetico")
except ArithmeticError:
    print("Error Aritemetico")
