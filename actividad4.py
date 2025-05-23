#Dada una lista de palabras, solicita al usuario una palabra y muestra si está o no en la lista.

palabras= ["casa", "carro", "perro", "gato", "computadora", "television" "mesa", "silla", "ventana", "puerta", "telefono"]
palabra_usuario= input("ingrese una palabra: ")

if palabra_usuario in palabras:
    print("la palabra está en la lista")
else:
    print("la palabra no está en la lista")
