'''
tuplas_1.py
script en Python que permita almacenar registros de las mascotas del usuario. Para cada mascota se solicitara el nombre, la edad, el peso y el tipo de mascota; dichos valores seran guardados en una tupla. Para permitir la posibilidad de tener varias mascotas se creara una lista en la cual se guarden los registros de cada mascota, es decir una lista de tuplas. El programadebera contar con un menu ciclico que permita registrar y consultar las mascotas.
'''
import os

REGISTRAR = 1
CONSULTAR = 2
SALIR  = 0

def mostar_menu():
    os.system('cls')
    print(f'''                          Mis Mascotas
    {REGISTRAR}) Registrar una mascota
    {CONSULTAR}) Consultar mascotas
    {SALIR}) Salir
    ''')

def registrar_mascota(mascotas):
    os.system('cls')
    print('                                Registar Mascota')
    nombre = input('Nombre: ')
    edad = int(input('Edad: '))
    peso = float(input('Peso: '))
    tipo = input('Tipo: ')
    mascotas.append( (nombre,edad,peso,tipo) )

def consultar_mascotas(mascotas):
    os.system('cls')
    print('                                 Mis Mascotas')
    if len(mascotas) == 0:
        print('Aun no has registrado mascotas')
    else:
        for mascota in mascotas:
            nombre, edad, peso, tipo = mascota
            print(f'''
            Nombre: {nombre} 
            Edad: {edad}
            Peso: {peso} 
            Tipo: {tipo}''')
            print(' ^.^ ´°.°`' *8)

def main():
    mis_mascotas = []
    continuar = True
    while continuar:
        try:
            mostar_menu()
            opc = int(input('Selecciona una opcion: '))

            if opc == REGISTRAR:
                registrar_mascota(mis_mascotas)
            elif opc == CONSULTAR:
                consultar_mascotas(mis_mascotas)
            elif opc == SALIR:
                continuar = False
            else:
                print('Opcion no valida.')
            input('ENTER para continuar...')
        except:
            print('Error eso es una letra')
            input('ENTER para continuar...')
        
if __name__ == '__main__':
    main()