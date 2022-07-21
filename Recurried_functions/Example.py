'''
Created on 31 may. 2020

@author: RSSpe
'''

def multiply(a, b):
    return a * b


def multby(func, num):
    return lambda y: func(num, y)


funcion = multby(multiply, 4)
print(funcion(2))

# ----------------------------------------

def verificarNumero(a, b):
    if a % b == 0:
        return "a es multiplo de b"
    return "a no es multiplo de b"


def obtener(verificarNumero, num):
    return lambda y: verificarNumero(num, y)
    

vn = obtener(verificarNumero, 4)
print(vn(2))
