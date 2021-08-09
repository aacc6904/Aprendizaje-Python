# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 18:51:44 2021

@author: USUARIO
"""

def mensaje():
    print("Ingrese el siguiente valor: ")
    
mensaje()
a=input()
mensaje()
b=input()
mensaje()
c=input()
mensaje()
d=input()


def saludos(nombre1,nombre2):
    print("Saludos: ",nombre1+ ", "+nombre2)
saludos("Aman Carrillo","Jose Tenorio")


def resta(a,b):
    print("la resta entre: ",a,"-",b,"es",a-b)
resta(5,2)
resta(b=2,a=5)


def resta(a,b):
    print("la resta entre: ",a,"-",b,"es",a-b)
resta(5,2)
resta(b=2,a=5)
resta(5,b=2)

def sumar(a,b):
    return a+b
def restar(a,b):
    return a-b
def multiplicar(a,b):
    return a*b
def dividir(a,b):
    return a/b
def exponencial(a,b):
    return a**b
x=float(input("Ingrese la variable x: "))
y=float(input("Ingrese la variable y: "))
print("")
Rsumar=sumar(x,y)
Rrestar=restar(x,y)
Rmultiplicar=multiplicar(x,y)
Rdividir=dividir(x,y)
Rexponencial=exponencial(x,y)
print("Los resultados son:")
print("Suma: ",Rsumar)
print("Restar: ",Rrestar)
print("Multiplicar: ",Rmultiplicar)
print("Dividir: ",Rdividir)
print("Exponencial: ",Rexponencial)

def creaLista(n):
    lista=[]
    for i in range (n):
        lista.append(i)
    return lista
numero=int(input("Ingrese el numero elementos de la lista: "))
print(creaLista(numero))