'''
repetitiva_mientras_3.py
script en Python que simule el sistema de validacion de datos de una plataforma
digital. Se le solicitara al usuario su nombre y contraseña mientras la informacion
proporcionada no coincidaa con la informacion previamente registrada.
'''
import os

NAME_USER = 'sebas'
PASSWORD = 'seba123'

# print('Registrate')
reName = input('Escribe tu nombre de usuario: ')
rePassword = input('Escribe tu contraseña: ')

while reName != NAME_USER:
    os.system('cls')
    print('Nombre de usuario incorrecto.')
    reName = input('Escribe tu nombre de usuario de nuevo: ')

while rePassword != PASSWORD:
    os.system('cls')
    print('Contraseña incorrecta. ')
    rePassword = input('Escribe tu contraseña de nuevo: ')

print('\nSesion iniciada con exito!.')