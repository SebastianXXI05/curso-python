"""
selectiva_simple_4.py
script en Python que pregunte ak usuario cuanto indica el termometro y si ese valor se encuentra entre 18 y 27 que le indique que la temperatura es agradable
"""

print("¿Cuanta temperatura indica el termometro?")
temperatura = int(input())

if temperatura >= 18 and temperatura <= 27:
    print("La temperatura es agradable")

else:
    print("La temperatura no es muy agradable")  