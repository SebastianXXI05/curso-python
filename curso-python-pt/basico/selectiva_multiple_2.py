"""
selectiva_multiple_2.py
script en python que muestre un menu con los nombres de distintos paises de America y
si el usuario selecciona alguna de las opciones te mostrara el nombre de la capital de ese pais.
"""

MEXICO = 1
URUGUAY = 2
COLOMBIA = 3
AGERTINA = 4
ECUADOR = 5
PERU = 6

print("'''                          Capitales de america                                               \n1) Mexico\n2) Uruguay\n3) Colombia\n4) Agertina\n5) Ecuador\n6) Peru'''")
opc = int(input("\nSelecciona una opcion: "))

if opc == MEXICO:
    print("Ciudad de Mexico")

elif opc == URUGUAY:
    print("Montevideo")

elif opc == COLOMBIA:
    print("Bogota")

elif opc == AGERTINA:
    print("Buenos Aires")

elif opc == ECUADOR:
    print("Quito")

elif opc == PERU:
    print("Quito")

else:
    print("Opcion no valida")

print("Que tengas un buen dia")