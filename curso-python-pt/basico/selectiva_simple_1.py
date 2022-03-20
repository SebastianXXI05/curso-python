"""
selectiva_simple_1.py
script en Python que solicite la edad al usuario y si esa edad es mayor o igual a 18 indique que es mayor de edad
"""

print("¿Cual es tu edad?")
edad = int(input())

if edad >= 18:
    print(f"Eres mayor de edad. Tienes {edad} años.")

else:
    print(f"Eres menor de edad. Tienes {edad} años.")