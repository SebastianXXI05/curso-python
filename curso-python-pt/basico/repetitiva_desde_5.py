'''
repetitiva_desde_5.py
script en Python que muestre las tablas de multiplicar de los numeros del 1 al 10. Cada tabla se muestra hasta el decimo multiplo.
'''
import os
os.system('cls')

for numero in range(1, 11):
    print(f'                            tabla de multiplicar del {numero}')
    for multiplo in range(1, 11):
        print(f'{numero} x {multiplo} = {numero * multiplo}')
        

print('Nos vemos.')