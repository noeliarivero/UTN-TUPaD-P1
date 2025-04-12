hemisferio = input("¿En qué hemisferio estás? (N/S): ").strip().upper()
mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))

if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"
elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"
elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"
elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"
else:
    estacion_norte = "Desconocida"
    estacion_sur = "Desconocida"

# Mostramos el resultado según el hemisferio
if hemisferio == "N":
    print("Estás en", estacion_norte)
elif hemisferio == "S":
    print("Estás en", estacion_sur)
else:
    print("Hemisferio no válido. Por favor ingrese N o S.")