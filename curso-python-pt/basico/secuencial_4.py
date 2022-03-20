"""
secuencial_4.py
script en python que solicite al usuario 2 numeros y
posteriormente muestre la suma de ambos valores.
"""

valor_1 = input("Ingresa un numero")
valor_1 = int(valor_1)

valor_2 = input("Ingresa otro numero")
valor_2 = int(valor_2) #conversion de tipo cadena(str) a entero(entero)

suma = valor_1 + valor_2

print(f"{valor_1} + {valor_2} = {suma}")