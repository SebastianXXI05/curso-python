"""
selectiva_simple_3.py
script en Python que solicite la calificacion y cantidad de asistencias a un curso. Si la calificacion es mayor o igual que 60 y la cantidad de asistencias es mayor a 20 entonces que le indique, que ha aprobado el curso.
"""

print("¿Cual es tu calificacion?")
calificacion = int(input())

print("¿Cual es tu cantidad de asistencias.?")
asistencia = int(input())

if calificacion >= 60 and asistencia >= 20:
    print("Muy bien aprobaste el curso.")
    if calificacion >= 95:
        print("Eres un estudiante sobresaliente.")

else:
    print("No aprobaste el curso.")