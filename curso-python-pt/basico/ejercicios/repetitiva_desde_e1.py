'''
repetitiva_desde_e1.py
script en Python que muestre un formato de 24 horas. El despliegue seguira el formato h:m:s. El cronometro
debera iniciar en 0:0:0 y pofra llegar hasta 23:59:59. Implementar retardos de 1 segundo y limpieza de forma
tal que solo se vea un tiempo en pantalla.
'''
import time
import os

for horas in range(24):
    os.system('cls')
    print(f'{horas}:0:0')
    time.sleep(1)

    if horas == 23:
        for minutos in range(60):
            os.system('cls')
            print(f'{horas}:{minutos}:0')
            time.sleep(0.2)

        if minutos == 59:
            for segundos in range(60):
                os.system('cls')
                print(f'{horas}:{minutos}:{segundos}')
                time.sleep(0.1)

print('Hasta luego')