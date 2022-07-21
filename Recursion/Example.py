'''
Created on 2 may. 2020

@author: RSSpe
'''

def factorial(n):
    if n == 1:
        return 1
    else:
        res = n*factorial(n-1)
        return res


print(factorial(5))

#Complementado
def factorial2(n, depth = 1):
    if n == 1:
        print('\t' * depth, 'Returning 1')
        return 1
    else:
        print('\t' * depth, 'Recursively calling factorial2 (', n-1, ')')
        res = n*factorial(n-1)
        print('\t' * depth, 'Returning: ', res)
        return res

print("Calling factorial 2")
print(factorial2(5))


# tail recursive
def tail_factorial(n, accumulator=1):
    if n == 0:
        return accumulator
    else:
        return tail_factorial(n-1, accumulator * n)
    
    
print(tail_factorial(5))

# ---------------------------------------------

lista = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

def sumar(lista, longitud):
    i = longitud - 1
    if i != 0:
        return lista[i] + sumar(lista, longitud-1)
    else:
        return lista[0]
    

print(sumar(lista, len(lista)))

