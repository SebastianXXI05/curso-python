import re
"""
secuencial_e1.py
script en python que cacule el area de un triangulo. El usuario debera ingresar el de la base como el de la altura y el programa mostrara el valor del area.
"""
def int_float(num):
    tipoDeNumero = re.search(r".+(\D).+", num)
    if tipoDeNumero:
        num = float(num)

    else:
        num = int(num)
    
    return num

print("Ingresa la base.")
base = int_float(input())

print("\nIngresa la altura.")
altura = int_float(input())

area = (base * altura) / 2

print(f"\nBase = {base} Altura = {altura} Area = {area}")