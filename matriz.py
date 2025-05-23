#matriz

matriz= [[1, 2], [3, 4]]
print("-" * 17)
for fila in matriz:
    for columna in fila:
        print(f"| {columna:>6}", end=" ")
    print( "|")
print("-" * 17)