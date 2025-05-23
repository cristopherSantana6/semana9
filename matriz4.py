#aumentar el valor de cada elemento de la matriz un 15%

matriz= [["300", "200", "100"], ["400", "500", "600"], ["700", "800", "900"]]
print("-" * 30)
for fila in matriz:
    for columna in fila:
        print(f"| {columna:>6}", end=" ")
    print( "|")
    print("-" * 30)
    
matriz_nueva= []
for fila in matriz:
    new_row= []
    for columna in fila:
        new_row.append(int(columna) * 1.15)
    matriz_nueva.append(new_row)
for fila in matriz_nueva:
    for columna in fila:
        print(f"| {columna:>6.1f}", end=" ")
    print( "|")
    print("-" * 30)