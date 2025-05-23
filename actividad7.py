#A partir de una lista de números reales, encuentra el mayor y el menor valor

numeros=[]

while True:
    try:
        numero=float(input("ingrese un numero real (o 'fin' para terminar): "))
        numeros.append(numero)
    except ValueError:
        if input("¿Desea terminar? (s/n): ").lower() == 's':
            break
        else:
            continue
    except Exception as e:
        print(f"Error inesperado: {e}")
        break   
print("lista de numeros reales: ", numeros)
if numeros:
    mayor = max(numeros)
    menor = min(numeros)
    print(f"El mayor valor es: {mayor}")
    print(f"El menor valor es: {menor}")
else:
    print("No se ingresaron números reales.")
    