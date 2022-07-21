'''
Created on 25 jun. 2020

@author: RSSpe
'''

# Implicit Contracts

class Quantity:
    def __init__(self, value=0):
        self.value = value

    def __gt__(self, other):
        if self.value > other.value:
            return True
        else:
            return False

    def __add__(self, other):
        new_value = self.value + other.value
        return Quantity(new_value)

    def __sub__(self, other):
        new_value = self.value - other.value
        return Quantity(new_value)

    def __mul__(self, other):
        new_value = self.value * other.value
        return Quantity(new_value)

    def __pow__(self, other):
        new_value = self.value ** other.value
        return Quantity(new_value)

    def __truediv__(self, other):
        new_value = self.value / other.value
        return Quantity(new_value)

    def __floordiv__(self, other):
        new_value = self.value // other.value
        return Quantity(new_value)

    def __mod__(self, other):
        new_value = self.value % other.value
        return Quantity(new_value)

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __ge__(self, other):
        return self.value >= other.value
    
    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __str__(self):
        return 'Quantity[' + str(self.value) + ']'

class Calculator:
    def add(self, x, y):
        return x + y


calc = Calculator()
print('calc.add(3, 4):', calc.add(3, 4))
print('calc.add(3, 4.5):', calc.add(3, 4.5))
print('calc.add(4.5, 6.2):', calc.add(4.5, 6.2))
print('calc.add(2.3, 7):', calc.add(2.3, 7))
print('calc.add(-1, 4):', calc.add(-1, 4))

q1 = Quantity(5)
q2 = Quantity(10)
print(calc.add(q1, q2))

# Duck typing

class Calculator2:
    """ Simple Calculator class"""
    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y
    
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        return x / y 

class Distance:
    def __init__(self, d):
        self.value = d
    
    def __add__(self, other):
        return Distance(self.value + other.value)

    def __sub__(self, other):
        return Distance(self.value - other.value)

    def __str__(self):
        return 'Distance[' + str(self.value) + ']'


calc2 = Calculator2()
d1 = Distance(6)
d2 = Distance(3)
print(calc2.add(d1, d2))
print(calc2.subtract(d1, d2))
print()
print()

# Other example

class Perro:
    def moverse(self):
        print("Caminar")

class Tiburon:
    def moverse(self):
        print("Nadar")

class Lobo:
    def moverse(self):
        print("Caminar")


class Animal:
    def __init__(self, miAnimal):
        self.miAnimal = miAnimal
        
    def accion(self):
        self.miAnimal.moverse() # No importa el tipo de dato a recibir solo que tenga el metodo que queremos


a = Animal(Perro())
a2 = Animal(Tiburon())
a3 = Animal(Lobo())
a.accion()
a2.accion()
a3.accion()
