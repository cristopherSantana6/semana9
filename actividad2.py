#Solicita 10 números al usuario, guárdalos en una lista y muestra la suma
#total.


lista_numeros= []

for i in range(10):
    numero=float(input(f"ingrese digito {i + 1}: "))
    lista_numeros.append(numero)
print("lista de 10 numeros: ", lista_numeros)
suma=0
for i in lista_numeros:
    suma+=i
print("la suma total es: ", suma)