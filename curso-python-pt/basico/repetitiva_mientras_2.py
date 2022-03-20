'''
repetitiva_mientras_2.py
script en Python que sume valores pares y multiplique valores impares mientras el usuario no ingrese
0. Se debera utilizar la estructura repetitiva "mientras" para solicitar al usuario un numero y
dependiendo del numero lo suma o lo multiplica.
'''

print('Escribe 0 para dejar de sumar y multiplicar')
num = int(input('Ingresa un numero '))
suma = 0
multipilicacion = 1

while num != 0:
    suma_o_multp = num % 2
    # print(comp)

    if suma_o_multp == 0:
        suma = suma + num

    else:
        multipilicacion = num * multipilicacion
    num = int(input('Ingresa un numero '))
    

print(f'\nsuma: {suma}') 
print(f'multiplicacion: {multipilicacion}') 
print('Que tengas un buen dia')