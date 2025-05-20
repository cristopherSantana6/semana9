array_str= ["uno", "dos", "tres", "cuatro", "cinco"]
print("array de strings: ", array_str)

#insertar un elemento al inicio del arreglo
array_str.insert(3, "cero")
print("array de cadenas despues de insertar: ", array_str)

#contar cuantos numeros haye en el arreglo
cantidad = len(array_str)
print("cantidad de cadenas en el arreglo: ", cantidad)

#eliminar un elemento del arreglo
array_str.remove("tres")
print("array de cadenas despues de eliminar 3: ", array_str)

#eliminar un elemento del arreglo
array_str.pop(2)
print("array de cadenas despues de eliminar 2: ", array_str)