#Dada una lista de 10 números, contar cuántos son mayores que 50.

numeros= []
contador=0

for i in range(10):
    numero= float(input(f"ingrese el digito {i + 1}: "))
    numeros.append(numero)
    if numero >50:
        contador+=1
    
print("lista de 10 numeros: ", numeros) 
print("la cantidad de numeros mayores que 50 es: ", contador)