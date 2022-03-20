"""
selectiva_doble_1.py
script en python que solicite al usuario adivinar un número entre 1 y 10.
si el usuario adivina entonces lo felicita por su logro; en caso contrario le indica cual
es el numero secreto.
"""
import random

secreto = random.randint(1,10)

print("Adivina el numero entre 1 y 10.")
usuario = int(input())

if usuario == secreto:
    print("Felicidades adivinaste.")

else:
    print(f"El numero era {secreto}")

print("Que tengas un buen dia.")