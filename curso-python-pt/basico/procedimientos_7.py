'''
procedimientos_7.py
script en Python que implemente un procedimiento dentro del cual se muestre la tabla de multiplicar de un numero recibido como argumento. El procedimiento contara con un segundo argumento que indicara hasta que multiplo se mostrara la tabla de multiplicar. Ese segundo argumento tendra como valor por omision el numero 10.
'''

def tablas(num,multiplo=10):
    print(f'''\n                        Tablas de multiplicar del numero {num}                  
    ''')
    for nums in range(1,multiplo+1):
        print(f'{num} x {nums} = {num * nums}')

tablas(2,20)
tablas(3)
print('Nos vemos...')