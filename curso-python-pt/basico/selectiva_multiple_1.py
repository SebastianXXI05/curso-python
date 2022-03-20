"""
selectiva_multiple_1.py
script en python que solicite al usuario una calificacion y una cantidad de asistencias
a un curso. Si la calificacion y la cantidad de asistencias son aprobatorias entonces se le
felicita por su logro en caso contrario se le indicara en que fallo. La calificasion minima
aprobaroria sera de 60 y la cantidad minima de asistencias sera de 24.
"""

MIN_CAL = 60
MIN_ASI = 24

print("Por favor ingresa los siguientes datos: ")
cal = int(input("\nCalificacion: "))
asi = int(input("Asistencias: "))

if cal >= MIN_CAL and asi >= MIN_ASI:
    print("\n¡Felicidades aprobaste este curso!")

elif cal < MIN_CAL and asi >= MIN_ASI:
    print(f"\nCalificacion insuficiente. El minimo es: {MIN_CAL}")

elif cal >= MIN_CAL and asi < MIN_ASI:
    print(f"\nAsistencias insuficientes. El minimo es: {MIN_ASI}")

else:
    print("Ni la calificacion y la cantidad de asistencias fueron suficientes")
print("Que tengas buen dia.")