'''
Created on 1 jul. 2020

@author: RSSpe
'''

# Generators

# Example

def gen_numbers():
    yield 1
    yield 2
    yield 3 


for i in gen_numbers():
    print(i)


# When Do the Yield Statements Execute?

def gen_numbers2():
    print('Start')
    yield 1
    print('Continue')
    yield 2
    print('Final')
    yield 3
    print('End')


for i in gen_numbers2():
    print(i)


# An Even Number Generator

def evens_up_to(limit):
    value = 0
    while value <= limit:
        yield value
        value += 2


for i in evens_up_to(6):
    print(i, end=', ')


# Nesting Generator Functions
print()
for i in evens_up_to(4):
    print('>>>i:', i)
    for j in evens_up_to(6):
        print('j:', j, end=', ')
    print('')


# Using Generators Outside a for Loop

# You do not need a for loop to work with a generator function; the generator object
# actually returned by the generator function supports the next() function. This
# function takes a generator object (returned from the generator function) and returns
#the next value in sequence.

evens = evens_up_to(4)
print(next(evens), end=', ')
print(next(evens), end=', ')
print(next(evens))

# Las llamadas posteriores a next (evens) no devuelven ningún valor; si es necesario el generador
# puede arrojar un error / excepción.
