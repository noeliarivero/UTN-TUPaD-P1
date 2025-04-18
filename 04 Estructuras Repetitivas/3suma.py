numMenor = int(input("Ingresá el numero más chico "))
numMayor = int(input("Ingresá el numero más grande "))
suma = 0

if numMenor < numMayor:
    numMenor += 1
    for numMenor in range(numMenor,numMayor):
        suma += numMenor 
elif numMenor > numMayor:
    numMayor += 1
    for numMayor in range(numMayor,numMenor):
        suma += numMayor 
else:
    print("Debe ingresar numeros distintos ")

print("La suma total es de ", suma )

