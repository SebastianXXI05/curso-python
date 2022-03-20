'''
listas_e.py
Hacer el juego del ahorcado con los paises de america.
'''
import os
import random

MAX_FALLOS = 5
paises = ['Antigua y Barbuda','Argentina','Bahamas','Barbados','Belice','Bolivia','Brasil','Canadá','Chile',' Colombia','Costa Rica','Cuba','Dominica','Ecuador','El Salvador','Estado Unidos','Granada','Guatemala','Guyana','Haití','Honduras','Jamaica','México','Nicaragua','Panamá','Paraguay','Perú','República Dominicana','San Cristóbal y Nieves','San Vicente y las Granadinas','Santa Lucia','Surinam','Trinidad y Tobago','Uruguay','Venezuela']

def crear_cadenas():
    pais = random.choice(paises)
    secreto = '_'*len(pais)
    return pais, secreto

def reemplazar_simbolo(original,secreto,simbolo):
    cantidad = original.count(simbolo)
    inicio = 0
    for i in range(cantidad):
        pos = original.find(simbolo, inicio)
        secreto = secreto[:pos] + simbolo + secreto[pos+1:]
        inicio = pos + 1
    return secreto

def ahorcado():
    print(f'Hola vamos a jugar el juego del ahorcado. \nLa palabra secreta sera el nombre de undo de los {len(paises)} del continente americano. \nTienes oportunidad de fallar hasta {MAX_FALLOS} veces. !Comencemos¡')
    input('presiona ENTER para comenzar...')
    # os.system('cls')
    original, secreto = crear_cadenas()
    fallos = 0

    while secreto != original and fallos < MAX_FALLOS:
        os.system('cls')
        print(f'palabra: {secreto}')
        s = input('¿Cual simbolo quieres destapar? ')
        if s in original:
            secreto = reemplazar_simbolo(original, secreto, s)
            print('¡Sigue haci! El simbolo es parte de la palabra')
        else:
            print('Lo siento el simbolo no es parte de la palabra')
            fallos += 1
        input('Presiona enter para continuar')
        os.system('cls')
    if secreto == original:
        print(f'Felicidades, el pais es {secreto}')
    else:
        print(f'Lo siento, el pais era {original}')
    print('Nos vemos...')

def main():
    ahorcado()

if __name__ == '__main__':
    main()