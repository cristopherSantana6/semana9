#matriz 3*3 nombres de amigos

matriz= [["Juan", "Pedro", "Luis"], ["Ana", "Maria", "Luisa"], ["Jose", "Carlos", "Javier"]]
print("-" * 30)
for fila in matriz:
    for columna in fila:
        print(f"| {columna:>6}", end=" ")
    print( "|")
    print("-" * 30)
    
cantidad_letras= []

for fila in matriz:
    new_row= []
    for columna in fila:
        new_row.append(len(columna))
    cantidad_letras.append(new_row)
    
for fila in cantidad_letras:
    for columna in fila:
        print(f"| {columna:>6}", end=" ")
    print( "|")
    print("-" * 30)