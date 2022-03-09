# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 11:52:27 2022

@author: CAROLINA
"""

rango = int(input("Indroduzca el maximo numero a buscar: "))

if rango % 10:
    print("El número que tecleo no es válido")
    rango = int(input("Indroduzca un numero multiplo de 10: "))

temp = 0
#aux = 0
i = rango*0.6+1
value = 0
terms = 0
while i <= rango:
    numero=i
    while numero != 1:
           if numero % 2:   
               #print("%d," % (numero), end = "")
               numero = 3 * numero + 1
           else:
               #print("%d," % (numero), end = "")
               numero //= 2
           terms += 1
    #print(terms, temp)
  
    if terms > temp:
        #aux += 1
        temp = terms
        value = i
    terms = 0
    i += 2

print("Para los numeros menores a", rango)
print("La secuencia mas larga se encuentra con el numero", value)
print("y tiene", temp, "pasos")