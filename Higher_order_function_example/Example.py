'''
Created on 10 jun. 2020

@author: RSSpe
'''

def apply(x, function):
    result = function(x)
    return result

def mult(y):
    return y * 10.0

print(apply(5, mult))

# -------------------------

def mult_by_two(num):
    return num * 2

def mult_by_five(num):
    return num * 5

def square(num):
    return num * num

def add_one(num):
    return num + 1

def apply2(num, func):
    return func(num)

print(apply(10, mult_by_five))
print(apply(10, square))
print(apply(10, add_one))
print(apply(10, mult_by_two))

# Functions returning functions

def make_checker(s):
    if s == 'even':
        return lambda n: n%2 == 0
    elif s == 'positive':
        return lambda n: n >= 0
    elif s == 'negative':
        return lambda n: n < 0
    else:
        raise ValueError('Unknown request')
    
f1 = make_checker('even')
f2 = make_checker('positive') 
f3 = make_checker('negative') 
print(f1(3))
print(f2(3))
print(f3(3))

# ----------------------------------

def make_function():
    def adder(x, y):
        return x + y
    return adder

f1 = make_function()
print(f1(3, 2))
print(f1(3, 3))
print(f1(3, 1))
