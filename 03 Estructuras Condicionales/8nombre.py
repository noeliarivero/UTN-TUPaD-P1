nombre = input("Ingresá tu nombre:")
numero = int(input("Ingresá el numero 1, 2 o 3:"))

if numero == 1:
    print(nombre.upper())
elif numero == 2:
    print(nombre.lower())
elif numero == 3:
    print(nombre.title())   
else:
    print("Ingrese un número válido")
