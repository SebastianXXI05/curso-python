'''
repetitiva_desde_4.py
script en Python que muestre la tabla de multiplicar de un numero ingresado por el usuario. El usuario temabien podra ingresar hasta que valor llegara la tabla de multiplicar.
'''
import os

os.system('cls')

num = int(input('¿De que numero deseas ver la tabla de multiplicar?: '))
tabla = int(input('¿Ahora elige hasta que multiplo deseas ver?.'))

print(f'                            Tabla del {num}')
for multiplo in range(1,tabla + 1):
    com = num * multiplo
    print(f'{num} x {multiplo} = {com}')