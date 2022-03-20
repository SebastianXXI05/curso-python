'''
repetitiva_desde_6.py
script en Python que muestre uno de los simbolos de una plabra o frase. Por ejemplo si la frase fuera
"Hola" se deberia imprimir:
H
o
l
a
'''
print('Los simbolos de tu frase/palabra son: ')
word = input('Ingresa una frase o palabra: ')

for simbolo in word:
    print(f'{simbolo}')

print('Nos vemos')