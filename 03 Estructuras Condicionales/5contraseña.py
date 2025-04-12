contraseña = input("Ingrese su contraseña entre 8 y 14 caracteres: ")
caracteres = len(contraseña)

if caracteres >= 8 and caracteres <= 14:
    print("La contraseña se creó correctamente")
else:
    print("Vuelve a intentarlo, recuerda que debe tener entre 8 y 14 caracteres")