#Pide 10 números al usuario, guárdalos en una lista e imprímelos en orden inverso.
numeros=[]

for i in range (10):
    numero=int(input(f"ingrese el digito {i + 1}: "))
    numeros.append(numero)

print("lista de 10 numeros: ", numeros)
numeros.reverse()
print(f"lista de 10 numeros en orden inverso: ", numeros)