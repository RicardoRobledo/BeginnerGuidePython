'''
Created on 29 may. 2020

@author: RSSpe
'''

# Numero primo
def is_prime(n, c):
    if c == 1:
        return True
    else:
        if n%c==0:
            return False
        else:
            return is_prime(n, c-1)


n=7
print("El numero es:", is_prime(n, n-1))

# -------------------------------------------
# Devolver lista
def devolverLista(num, lim, c=[]):
    if num == 0:
        return 0
    c.append(devolverLista(num-1, lim))
    if num == lim:
        return c
    return num


num = 10
print("Lista:", devolverLista(num+1, num+1))

# --------------------------------------------
# Devolver lista con rango
def devolverListaConRango(inicio, fin, c=[]):
    if inicio == fin:
        return fin
    c.append(devolverListaConRango(inicio+1, fin))
    if len(c) == fin-1:
        return c
    return inicio


rango = (2, 4)
lista = devolverListaConRango(rango[0]-1, rango[1])
lista.reverse()
print("Lista:", lista)

# --------------------------------------------
# Suma
def sumar(n):
    if n == 1:
        return 1
    return n+sumar(n-1)
    

n = 5
print("Suma:", sumar(n))

# --------------------------------------------
# remover elemento
def removerTodos(tupla, cont=0):
    if cont == len(tupla[0]):
        return 
    

elemento = 4
lista = [1, 0, 2, 4, 3, 5, 6, 4, 8, 9, 6, 4, 7, 3, 2, 4]
tupla = (lista, elemento)
print(tupla)
print(removerTodos(tupla))

# --------------------------------------------
# Fibonacci
def fibonacci(val, val2, limit):
    if limit!=0:
        print(val)
        tmp=val2
        val2+=val
        val=tmp
        fibonacci(val, val2, limit-1)


fibonacci(0, 1, 11);
