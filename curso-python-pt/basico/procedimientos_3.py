'''
procedimientos_3.py
script en Python que dentro de un procediemiento solicite el nombre y la edad del usuario y en caso de ser mayor o igual que 18 le indique
que es mayor de edad, en caso contrario indicarle que aun es menor.
'''

def mayoria_edad():
    name = input('¿Cual es tu nombre? ')
    old = int(input('¿Cual es tu edad? '))
    if old >= 18:
        print(f'Eres mayor de edad, {name}')
    else:
        print(f'Eres menor de edad, {name}')

mayoria_edad()