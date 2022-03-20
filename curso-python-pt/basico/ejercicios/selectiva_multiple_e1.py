"""
script en Python que permita al usuario, elegir si quiere sumar, restar, multiplicar, dividir.
Y tambien preguntarle cuales valores númericos quiere usar. 
"""

SUMA = 1
RESTA = 2
MULTIPLICACION = 3
DIVISION = 4

print("Elige que operacion quieres hacer: \n1) Sumar \n2) Restar \n3) Multiplicar \n4) Dividir")

opc = int(input("Elige una opcion: "))

#SUMA
if opc == SUMA:
    num1 = int(input("Ingresa un numero. "))
    num2 = int(input("Ingresa otro numero para sumar. "))

    res = num1 + num2
    print(f"\nEl resultado de tu suma es: {res}")

#RESTA
elif opc == RESTA:
    num1 = int(input("Ingresa un numero. "))
    num2 = int(input("Ingresa otro numero para restar. "))

    res = num1 - num2
    print(f"\nEl resultado de tu resta es: {res}")

#MULTIPLICACION
elif opc == MULTIPLICACION:
    num = int(input("Escribe los numeros que quieres multiplicar. "))  
    multipicador = int(input("Escribe por cual numero lo quieres multiplicar. "))  

    res = num * multipicador
    print(f"\nEl resultado de tu multiplicacion es: {res}")

#DIVISION
elif opc == DIVISION:
    num = int(input("Escribe un numero. "))
    divisor = int(input("Elige el numero por el que quieres dividir. "))
    if divisor == 0:
        print("¡No puedes dividir por '0'!")
    
    res = num / divisor
    print(f"\nEl resultado de tu division es: {res}")

else:
    print("Elije una opcion valida, vuelve a intentar.")

print("\nQue tengas un buen dia.")