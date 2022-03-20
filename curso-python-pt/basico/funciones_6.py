'''
funciones_6.py
script en Python que convierte  en segundos minutos.
'''

def segundos_a_minutos(segundos):
    m = segundos // 60
    s = segundos % 60 
    return m, s

print('Pragrama que convierte segundos en minutos.')
seg = int(input('Segundos a convertir: '))

min, segu = segundos_a_minutos(seg)

print(f'El equivalente es: {min}:{segu}')