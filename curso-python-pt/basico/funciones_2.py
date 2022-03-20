'''
funciones_2.py
script en Python que implemente una funcion encargada de calcular el inidice de masa corporal del usuario.
'''

def calcular_IMC():
    peso = float(input('Peso: '))
    estatura = float(input('Estatura: '))
    imc = peso / (estatura ** 2)
    return imc

print('Vamos a calcular tu IMC')
imc = calcular_IMC()
print(f'Indice de masa corporal es: {imc :.2f}') #corta el numero de decimales que aparecen {imc :.4f}')