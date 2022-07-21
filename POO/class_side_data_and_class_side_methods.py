'''
Created on 10 jun. 2020

@author: RSSpe
'''
# Class side data
class Person:
    """ An example class to hold a persons name and age"""
    instance_count = 0
    
    def __init__(self, name, age):
        Person.instance_count += 1 
        self.name = name 
        self.age = age
        
    def __del__(self):
        pass

p1 = Person('Jason', 36)
p2 = Person('Carol', 21) 
p3 = Person('James', 19) 
p4 = Person('Tom', 31)
del p4
print(Person.instance_count)

print('id(p1):', id(p1))
print('id(p2):', id(p2))

# The same reference for "p1" and "px"
px = p1
print(p1)
print(px)
print('id(p1):', id(p1))
print('id(px):', id(px)) 

# Class side methods

#Class-side methods should only perform one of the following roles: 
#
# • Instance creation This role is very important as it is how you can use a class as a factory for objects and can help hide a whole load of set up
# and instantiation work. 
#
# • Answering enquiries about the class This role can provide generally useful objects, frequently derived from class variables. For example, they may
# return the number of instances of this class that have been created. 
#
# • Instance management In this role, class-side methods control the number of instances created. For example, a class may only allow a single instance
# of the class to be created; this is termed a singleton class. Instance management methods may also be used to access an instance 
# (e.g. randomly or in a given state).
#
# • Examples Occasionally, class methods are used to provide helpful examples which explain the operation of a class. This can be very good practice. 
#
# • Testing Class-side methods can be used to support the testing of an instance of a class. You can use them to create an instance, perform an operation
# and compare the result with a known value. If the values are different, the method can report an error. This is a very useful way of
# providing regression tests. 
#
# • Support for one of the above roles. Any other tasks should be performed by an instance method.

class Person2: 
    """ An example class to hold a persons name and age"""
    instance_count = 0 
    
    @classmethod 
    def increment_instance_count(cls): 
        cls.instance_count += 1
        
    def __init__(self, name, age):
        self.name = name
        self.age = age 

Person2.increment_instance_count()
Person2.increment_instance_count()
Person2.increment_instance_count()
Person2.increment_instance_count()
print(Person2.instance_count)

# The class object is the base (root) class for all classes in Python.It has methods that are therefore available in all Python objects.
# It deﬁnes a common set of special methods and intrinsic attributes. The methods include the special methods:
# __str__(), __init()__, __eq__() (equals) and __hash__() (hash method). It also deﬁnes attributes such as __class__,__dict__,__doc__and__module__.
