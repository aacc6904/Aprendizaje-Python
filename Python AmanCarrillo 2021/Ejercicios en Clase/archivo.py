# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 20:36:15 2021

@author: USUARIO
"""

file=open("C:\\Users\\USUARIO\\Desktop\\archivo.txt")
for item in file:
    print(item)
file.close()
    

file=open("C:\\Users\\USUARIO\\Desktop\\archivo.txt")
for item in file:
    item=item.strip()
    print(item)
file.close()


lista=[]
file=open("C:\\Users\\USUARIO\\Desktop\\archivo.txt")
for item in file:
    item=item.strip()
    lista.append(item)
    print(item)
print(lista)
file.close()
