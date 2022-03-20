'''
pila_1.py
script en python que solicite al usuario escribir una expresion aritmetica y el programa le indique si dicha
expresion esta balanceada, es decir, si tiene la misma cantidad de parentesis de apertura y cierre.
'''

def validar_expresion(expresion):
    pila = []
    for simbolo in expresion:
        if simbolo == '(':
            pila.append('(')
        elif simbolo == ')':
            if len(pila) > 0:
                pila.pop()
            else:
                return False
    return len(pila) == 0

def main():
    print('Escribe una expresion aritmetica y te indicare si esta balanceada con respecto a parentesis.')
    e = input('Expresion: ')
    validar = validar_expresion(e)
    if validar:
        print('La expresion esta balanceada.')
    else:
        print('La expresion no esta balanceada')
    print('Nos vemos')

if __name__ == '__main__':
    main()