# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 11:26:11 2022

@author: CAROLINA
"""

numero = int(input("Indroduzca un número entero positivo: "))

if numero < 0:
    print("El número que tecleo no es válido")
else:
    while numero != 1:
       if numero % 2:   
           print("%d," % (numero), end = "")
           numero = 3 * numero + 1
       else:
           print("%d," % (numero), end = "")
           numero //= 2

       if numero == 1:
            print("1")
            
            

