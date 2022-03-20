'''
funciones_5.py
calculo de indice corporal
'''

def calcular_IMC(peso,estatura):
    return peso / (estatura **2)

print('Programa que calcula el indice de masa corporal.')
print('Ingresa los siguientes datos')
p = float(input('Peso: '))
e = float(input('Estatura: '))

print(f'IMC = {calcular_IMC(p,e):.2f}')