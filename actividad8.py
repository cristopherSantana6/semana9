#Dada una lista con valores repetidos, crea una nueva lista sin duplicados.

lista1=[]

for i in range(10):
    lista1.append(input("ingrese un valor: "))
print("lista 1:", lista1)
lista2=[]
for i in lista1:
    if i not in lista2:
        lista2.append(i)
print("lista 2:", lista2)