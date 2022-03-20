'''
argumentos.py
script en Python que implemente un procedimiento de menu generico.
'''

def menu(titulo,*args,**kwargs):
    print(f'                    {titulo}')
    for i in range(len(args)):
        print(f'{i+1}) {args[i]}')
    opc = int(input('Selecciona una opcion: '))
    if 1 <= opc <= len(args):
        print(f'Seleccionaste la opcion {args[opc-1]}')
    else:
        print('Opcion no valida')
        if 'error' in kwargs:
            print(f'{kwargs["error"]}')

menu('Operaciones aritmeticas', 'suma', 'resta', 'multiplicacion', error='No existe tal operacion')

print('Nos vemos...')