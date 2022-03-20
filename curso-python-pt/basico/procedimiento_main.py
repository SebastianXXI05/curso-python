'''
procedimiento_main.py
'''

def saludo_perzonalizado(name):
    print(f'Gusto en verte {name}')

def main():
    usuario = input('¿Hola como te llamas? ')
    saludo_perzonalizado(usuario)

if __name__ == '__main__':
    main()