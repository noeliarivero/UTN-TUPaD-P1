numero = str(input("Ingresá el número para saber sus dígitos: "))
digitos = len(numero) # está bien usar esta función acá? o tengo que averiguar los digitos sin función de por medio?
contador_digitos = 0;

if digitos > 0:
    for contador_digitos in range(digitos):
        contador_digitos += 1

print("Este numero tiene ", contador_digitos, " dígitos")
