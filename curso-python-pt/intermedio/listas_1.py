'''
listas_1.py
script en python que permita administrar operaciones sobre una lista. Dentro del programa existira una lista
para almacenar el nombre de distintas frutas. Para el control de la lista se mostrara un menu con las
siguientes opciones:
Agregar
Insertar
Mostrar lista
Buscar una fruta
Eliminar un registro
Ordenar lista
Limpiar lista
Salir
'''
import os

frutas = []

AGREGAR = 1
INSERTAR = 2
MOSTRAR = 3
BUSCAR = 4
ELIMINAR = 5
ORDENAR = 6
LIMPIAR = 7
SALIR = 0

def imprimir_menu():
    os.system('cls')
    print(f'''                              Frutas
    {AGREGAR}) Agregar
    {INSERTAR}) Insertar
    {MOSTRAR}) Mostrar
    {BUSCAR}) Buscar
    {ELIMINAR}) Eliminar
    {ORDENAR}) Ordenar
    {LIMPIAR}) Limpiar lista
    {SALIR}) Salir''')

def agregar_registro():
    print('                                 Agregar')
    nombre = input('Nombre: ')
    frutas.append(nombre)
    print('Registro agregado con exito.')

def insertar_registro():
    print('                                 Insertar')
    nombre = input('Nombre: ')
    pos = int(input('posicion: '))
    frutas.insert(pos, nombre)
    print('Registro insertado en la posicion indicada')

def mostrar_registros():
    print('                                 Mostrar')
    if len(frutas) > 0:
        for fruta in frutas:
            print(fruta)
    else:
        print('No se han agregado frutas a la lista')

def buscar_registro():
    print('                                 Buscar')
    if len(frutas) > 0:
        nombre = input('Nombre a buscar: ')
        if nombre in frutas:
            cantidad = frutas.count(nombre)
            inicio = 0
            for i in range(cantidad):
                pos = frutas.index(nombre, inicio)
                print(f'{nombre} se encuentra en la posicion {pos+1}')
                inicio = pos + 1
        else:
            print(f'{nombre} no ha sido registrado en la lista.')

    else:
        print('No se han agregado frutas a la lista')

def eliminar_registro():
    print('                                 Registro')
    if len(frutas) > 0:
        for i in range(len(frutas)):
            print(f'{i+1}. {frutas[i]}')
        print('0. Cancelar')
        pos = int(input(f'posicion a eliminar (1 - {len(frutas)}): '))

        if 0 < pos <= len(frutas):
            frutas.pop(pos-1)
            print('Registro elmininado con exito')
        else:
            print('No se eliminara nungun registro')
    else:
        print('No se han agregado frutas a la lista')

def ordenar_registros():
    print('                                 Ordenar')
    if len(frutas) > 0:
        frutas.sort()
        print('Registros ordenados alfabeticamente.')
    else:
        print('No se han agregado frutas a la lista')

def limpiar_registros():
    print('                                 Limpiar')
    frutas.clear()
    print('Los registros han sido borrados.')

def main():
    continuar = True
    while continuar:
        imprimir_menu()
        opc = int(input('Selecciona una opcion: '))
        os.system('cls')

        if opc == AGREGAR:
            agregar_registro()
        elif opc == INSERTAR:
            insertar_registro()
        elif opc == MOSTRAR:
            mostrar_registros()
        elif opc == BUSCAR:
            buscar_registro()
        elif opc == ELIMINAR:
            eliminar_registro()
        elif opc == ORDENAR:
            ordenar_registros()
        elif opc == LIMPIAR:
            limpiar_registros()
        elif opc == SALIR:
            print('Nos vemos...')
            continuar = False
        else:
            print('Opcion no valida.')
        input('ENTER para continuar.')

if __name__ == '__main__':
    main()