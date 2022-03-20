'''
funciones_3.py
script en Python que implemente una funcion encargada de convertir grados fahrenheit a celsius.
'''

def farenheit_a_celcius():
    f = float(input('Grados Farenheit: '))
    c =(f-32)/1.8
    return c

print('Programa que convierte grados Farenheit a celcius')
celcius = farenheit_a_celcius()

print(f'Celcius: {celcius :.2f}')
print('Nos vemos...')