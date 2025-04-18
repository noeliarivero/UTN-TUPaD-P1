positivo = 0
negativo = 0
par = 0
impar = 0

for i in range(0,100):
    num = int(input("Ingresá un número "))
    if num > 0:
        positivo += 1
        if num % 2 == 0:
            par += 1
        else:
            impar += 1
    elif num < 0:
        negativo += 1
        if num % 2 == 0:
                par += 1
        else:
                impar += 1
    else:
        print("El numero no puede ser 0")
        
print("Numeros positivos: ", positivo)
print("Numeros negativo: ", negativo)
print("Numeros pares: ", par)
print("Numeros impares: ", impar)