'''
cola_1.py
script en Python que permita al usuario registrar eventos en su agenda; cada evento se agregara en una cola
de prioridad salgan primero de la estructura. Para manejar la agenda se le mostrara al usuario un menu con 
las opciones de agregar evento y atender evento.
'''
import os
import queue

AGENDAR = 1
ATENDER = 2
SALIR = 0

def mostrar_menu():
    os.system('cls')
    print(f'''                               Mi Agenda
        {AGENDAR}) Agendar evento
        {ATENDER}) Atender evento
        {SALIR}) Salir
    ''')

def agendar_evento(ag):
    print('                                 Agendar Evento')
    evento = input('Evento: ')
    ag.put(evento)

def atender_evento(ag):
    print('                                 Atender Evento')
    if ag.empty():
        print('No hay eventos por atender')
    else:
        evento = ag.get()
        print(f'Evento: {evento}')

def main():
    agenda = queue.PriorityQueue()
    continuar = True
    while continuar:
        mostrar_menu()
        opc = int(input('Selecciona una opcion: '))
        os.system('cls')
        
        if opc == AGENDAR:
            agendar_evento(agenda)
        elif opc == ATENDER:
            atender_evento(agenda)
        elif opc == SALIR:
            continuar = False
            # print('Nos vemos...')
        else:
            print('Opcion no valida')
        input('Presiona ENTER para continuar...')
    print('Nos vemos...')

if __name__ == '__main__':
    main()