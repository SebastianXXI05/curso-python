"""
selectiva_simple_2.py
script en Python que genere un numero aleatorio entre 1 y 10 y le pida al usuario que intente adivirnalo. Si adivina el numero que lo felicite por su logro.
"""
#Agrega el modulo ramdo en el programa y con ello me permite generar numeros aleatorios
import random

secreto = random.randint(1, 10)
print("Encuentra el numero secreto, que esta entre 1 y 10")

numero = int(input())

if numero == secreto:
    print(f"Muy bien adivinaste el numero es: {secreto}")

else:
    print(f"\nSigue disfrutando tu dia. El numero es {secreto}")