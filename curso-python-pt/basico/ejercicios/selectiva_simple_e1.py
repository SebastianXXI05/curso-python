"""
selectiva_simple_e1.py
script en Python que redondea una calificacion.
"""

print("Ingresa tu calificacion")
calificacion = int(input())
residuo = calificacion % 10
mensaje = "Tu calificacion no amerita redondeo."

if 0 <= calificacion <= 100 and residuo >= 6:
    calificacion = calificacion + (10 - residuo)
    mensaje = f"Tu calificaion es: {calificacion}"

print(mensaje)
print("Que tengas un buen dia.")