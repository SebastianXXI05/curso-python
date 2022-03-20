'''
repetitiva_desde_1.py
script en Python que imprima los numeros pares desde el 2 hasta el 20 haciendo uso de un ciclo for.
'''

print('Programa que muestra los numeros pares del 2 al 20')
for num in range(2,21):
    comp = num % 2

    if comp == 0:
        print(f'numeros pares {num}')