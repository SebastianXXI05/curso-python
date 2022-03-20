'''
anidamiento_estructural.py
script en Python
'''
print('Bienvenid@ pongamos a prueba tu conocimineto :v')
respuesta = int(input('¿Cual es la velocidad de la luz en m/s? '))

if respuesta == 299792458:
    print('Correcto')
    respuesta = int(input('¿Cuanto es 8+8/8*8? '))

    if respuesta == 8+8/8*8:
        print('!Correcto¡')
        respuesta = input('¿De que color eran las mangas de chaleco de Napoleon? ')

        if respuesta == 'Los chalecos no tienen mangas':
            print('Felicidades te has llevado un millon de pesos')
        
        else:
            print('Lo siento, respuesta incorrecta')

    else:
        print('Lo siento, respuesta incorrecta')

else:
    print('Lo siento respuesta incorrecta')

print('Que tengas un buen dia')