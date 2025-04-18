num = input("Ingresá el numero a invertir")
numInvertido = 0 

while numero > 0:
    digito = numero % 10
    numero_invertido = numero_invertido * 10 + digito
    numero = numero // 10

print("El número invertido es:", numero_invertido)