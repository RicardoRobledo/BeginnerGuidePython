'''
Created on 11 jun. 2020

@author: RSSpe
'''
class Person:
    """ An example class to hold a persons name and age"""
    instance_count = 0
    
    def __init__(self, name, age):
        Person.instance_count += 1 
        self.name = name 
        self.age = age

p1 = Person('Jason', 36)
p2 = Person('Carol', 21) 
p3 = Person('James', 19) 
p4 = Person('Tom', 31) 
print(Person.instance_count)

# Intrinsic Attributes

# Classes have the following intrinsic attributes: 
#• __name__ the name of the class
#• __module__ the module (or library) from which it was loaded
#• __bases__ a collection of its base classes (see inheritance later in this book)
#• __dict__ a dictionary (a set of key-value pairs) containing all the attributes (including methods)
#• __doc__ the documentation string. 
#
# For objects:
# • __class__ the name of the class of the object
# • __dict__ a dictionary containing all the object’s attributes

print('Class attributes')
print(Person.__name__)
print(Person.__module__)
print(Person.__doc__)
print(Person.__dict__)
print('Object attributes')
print(p1.__class__)
print(p1.__dict__)
