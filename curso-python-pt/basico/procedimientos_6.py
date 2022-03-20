'''
procedimientos_6.py
script en Python que implemente un procedimiento que reciba el nombre y la edad del usuario y en el caso que la edad sea mayor o igual a 18 le indique que ya es mayor de edad; en caso contrario le indique que es menor de edad
'''

def edad(name,old):
    if old >= 18:
        print(f'Eres mayor de edad, {name}')
    else:
        print(f'Eres menor de edad, {name}')

edad('sebastian', 18)
edad( old=18, name='carlos')
print('Nos vemos')