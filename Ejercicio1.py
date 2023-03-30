print("Infracciones del Mes")
print("************************")

infracciones = int (input("Ingrese el numero de infraciones en el mes :"))

infracciones_diarias = infracciones / 30

matutino = infracciones * 0.2
vespertino = infracciones * 0.35
nocturno = infracciones * 0.45

print("El Promedio de Infracciones Matutinas es: ", matutino)
print("El Promedio de Infracciones Vespertinas es: ", vespertino)
print("El Promedio de Infracciones Nocturnas es: ", nocturno)

print("FIN PROGRAMA")
