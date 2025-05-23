#Suma los elementos que se encuentran en posiciones pares de la lista.

lena = int(input("Ingrese la longitud de la lista: "))
lista = []
for i in range(lena):
    lista.append(int(input("Ingrese un número: ")))
print("Lista:", lista)
suma = 0
for i in range(len(lista)):
    if i % 2 != 0:
        suma += lista[i]
print("La suma de los elementos en posiciones pares es:", suma)

#señalar posiciones pares e impares de la lista al pedir los numeros
