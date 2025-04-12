frase = input("Ingresa tu palabra o frase")

if frase[-1].lower() in "aeiou":
    frase += "!"

print("Resultado:", frase)