'''
Created on 11 jun. 2020

@author: RSSpe
'''

# Operator | Expression | Method
# Addition | q1 + q2 | __add__(self, q2)
# Subtraction | q1 – q2 | __sub__(self, q2)
# Multiplication | q1 * q2 | __mul__(self, q2)
# Power | q1 ** q2 | __pow__(self, q2)
# Division | q1 / q2 | __truediv__(self, q2)
# Floor | Division q1 // q2 | __ﬂoordiv__(self, q2)
# Modulo(Remainder) | q1 % q2 | __mod__(self, q2)
# Bitwise Left Shift | q1 << q2 | __lshift__(self, q2)
# Bitwise Right Shift | q1 >> q2 | __rshift__(self, q2)

# Unaries
# -   __neg__(self)
# +   __pos__(self)
# abs()   __abs__(self)
# ~   __invert__(self)
# complex()   __complex__(self)
# int()   __int__(self)
# long()   __long__(self)
# float()   __float__(self)
# oct()   __oct__(self)
# hex()   __hex__(self)

# Extended assignments
# +=   __iadd__(self, other)
# -=   __isub__(self, other)
# *=   __imul__(self, other)
# /=   __idiv__(self, other)
# //=   __ifloordiv__(self, other)
# %=   __imod__(self, other)
# **=   __ipow__(self, other)
# <<=   __ilshift__(self, other)
# >>=   __irshift__(self, other)
# &=   __iand__(self, other)
# ^=   __ixor__(self, other)
# |=   __ior__(self, other)

# Comparison
# <   __lt__(self, other)
# <=   __le__(self, other)
# ==   __eq__(self, other)
# !=   __ne__(self, other)
# >=   __ge__(self, other)
# >   __gt__(self, other)

# Others
# ^ | q1 ^ q2 | __xor__(self, q2)
# & | q1 & q2 | __and__(self, q2)
# | | q1 | q2 | __or__(self, q2)

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


q1 = Quantity(10)
q2 = Quantity(5)
print(q1 + q2)
print(q1 > q2)
