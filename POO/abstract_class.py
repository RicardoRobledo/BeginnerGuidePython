'''
Created on 11 jun. 2020

@author: RSSpe
'''
# Abstract class

from abc import ABC, abstractmethod

class EstructuraAbstracta(ABC):
    @abstractmethod
    def obtener(self):
        pass

    @abstractmethod
    def agregar(self):
        pass
    
class Estructura(EstructuraAbstracta):
    def obtener(self):
        pass
    
    def agregar(self):
        pass

a = Estructura()

# -------------------------------------

from abc import ABCMeta, abstractmethod

from abc import ABCMeta, abstractmethod

class Shape(metaclass=ABCMeta):
    def __init__(self, id):
        self._id = id

    @abstractmethod
    def display(self): pass

    @property
    @abstractmethod
    def id(self): pass

class Circle(Shape):
    def __init__(self, id):
        super().__init__(id)
        
    def display(self):
        print('Circle: ', self._id)
        
    @property
    def id(self):
        """ the id property """
        return self._id

    
c = Circle("circle1")
print(c.id)
c.display()

# ---------- Virtual subclasses --------------

from abc import ABCMeta

class Person(metaclass=ABCMeta):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def birthday(self):
        print('Happy Birthday')
        
class Employee(object):
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        
    def birthday(self):
        print('Its your birthday')

Person.register(Employee) # Here we now register the class Employee as a virtual subclass of the class Person
print(issubclass(Employee, Person))
e = Employee('Megan', 21, 'MS123')
print(isinstance(e, Person))

# This provides a very useful level of flexibility that can be exploited when using existing libraries and frameworks.

# ------------------------ Mixins ------------------------------

class PrinterMixin(metaclass=ABCMeta):
    def print_me(self):
        print(self)

class IDPrinterMixin(metaclass=ABCMeta):
    def print_id(self):
        print(self.id)

class Person2(object):
    def __init__(self, name):
        self.name = name
        
class Employee2(Person, PrinterMixin, IDPrinterMixin):
    def __init__(self, name, age, id2):
        super().__init__(name)
        self.age = age
        self.id = id
        
    def __str__(self):
        return 'Employee(' + self.id + ')' + self.name + '[' + str(self.age) + ']'


e = Employee2('Megan', 21, 'MS123')
e.print_me()
e.print_id()
