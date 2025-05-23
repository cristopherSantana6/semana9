#Solicita al usuario 8 calificaciones, guárdalas en una lista y calcula el promedio
calificaciones= []
for i in range(8):
    calificacion = float(input(F"ingrese la calificacion #{i + 1}: "))
    calificaciones.append(calificacion)
    promedio = sum(calificaciones) / len(calificaciones)

print("el promedio es: ", promedio)