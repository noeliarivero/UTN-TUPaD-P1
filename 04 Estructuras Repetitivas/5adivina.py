import random
num = int(random.randint(0,9))
numUsuario = int(input("Ingresá un num del 0 al 9 "))
intento = 1

while numUsuario != num:
    intento += 1
    numUsuario = int(input("Intenta otra vez! Vuelve a ingresar un num del 0 al 9 "))

print("Excelente! Haz acertado, lo intentaste ", intento , " veces")