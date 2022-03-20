"""
selectiva_doble_2.py
script en python que simule el sistema de validacion de una plataforma digital. El usuario
debera proporcionar tanto su nombre como la contraseña. Si coinciden los valores previamente
almacenados, entonces se le dara la bienvenida, si no se le indica que hubo un error.
"""

USER = "sebastian5"
PASSWORD = "sebas123"

print("Proporciona los siguientes datos:")
user = input("Usuario: ")
password = input("Contraseña: ")

if user == USER and password == PASSWORD:
    print("\n                 insta[°]")
    print("Bienvenid@")

else:
    print("\nDatos incorrectos, intenta de nuevo.")

print("Que tengas un buen dia.")