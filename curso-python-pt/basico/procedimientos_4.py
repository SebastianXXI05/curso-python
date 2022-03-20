'''
procedimientos_4.py
script en Python que muestre un menu ciclico; dicho menu sera implementado en un procedimiento.
'''

import os

ESP = 1
ING = 2
NO_SUBS = 3
SALIR = 4

def mostrar_menu():
    print(f'''                          Subtitulos
        {ESP}) Español
        {ING}) Ingles
        {NO_SUBS}) Sin subtitulos
        {SALIR}) Salir
    ''')

continuar = True
while continuar:
    os.system('cls')
    mostrar_menu()
    opc = int(input('Selecciona una opcion: '))
    os.system('cls')

    if opc == ESP:
        print('Subtitulos en español')
    elif opc == ING:
        print('Subtitulos en ingles')
    elif opc == NO_SUBS:
        print('Sin subtitulos')
    elif opc == SALIR:
        continuar = False
    else:
        print('Opcion no valida')
    input('Presiona enter para continuar...')

print('Adios')