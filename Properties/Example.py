'''
Created on 22 jun. 2020

@author: RSSpe
'''

# Syntax: <property_name> = property(fget=None, fset=None, fdel=None, doc=None)

class Person: 
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if isinstance(new_age,int) & new_age > 0 & new_age < 120:
            self._age = new_age

    age = property(get_age, set_age, doc="An age property")

    def get_name(self):
        return self._name

    name = property(get_name, doc="A name property")

    def __str__(self):
        return 'Person[' + str(self._name) +'] is ' + str(self._age)


person = Person('John', 54)
print(person)
print(person.age)
print(person.name)
person.age = 21
print(person)

# -----------------------------------------------------------------
# More Concise Property Deﬁnitions
#
# Python have three new decorators @property, @<propertyname>.setter and @<propertyname>.deleter
# The documentation string is now deﬁned in the method associated with the @property decorator
# (providing this documentation string is usually considered good practice).

class Numero(object):
    def __init__(self):
        self.__numero = 4
    
    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, valor):
        self.__numero = valor


num = Numero()
print(num.numero)
num.numero = 44
print(num.numero)
