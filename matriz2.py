#matriz flotante

matriz= [[1.2, 2.3], [3.4, 4.5]]

print("-" * 17)
for fila in matriz:
    for columna in fila:
        print(f"| {columna:>6.1f}", end=" ")
    print( "|")
print("-" * 17)