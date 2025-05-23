#Llena una lista con 10 números enteros aleatorios entre 1 y 100, y sepáralos en dos listas: pares e impares.

import random
lista=[]
lista_pares=[]
lista_impares=[]

for i in range(10):
    lista.append(random.randint(1,100))
    
    if lista[i] % 2 == 0:
        lista_pares.append(lista[i])
    else:
        lista_impares.append(lista[i])
     
       
print("lista:", lista)
print("lista pares:", lista_pares)
print("lista impares:", lista_impares)