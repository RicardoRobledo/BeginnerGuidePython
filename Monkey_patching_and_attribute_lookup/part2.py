'''
Created on 30 jun. 2020

@author: RSSpe
'''

# Handling Unknown Attribute Access

# __getattr__(); this method will be called when an attribute is not found in the
# objects (and classes) __dict__ dictionary. This method can then perform whatever
# action is appropriate such as logging a message or providing a default value etc

class Student:
    count = 0
    
    def __init__(self, name):
        self.name = name
        Student.count += 1

    # Method called if attribute is unknown
    def __getattr__(self, attribute):
        print('__getattr__: ', attribute)
        return 'default'


student = Student('John')
res1 = student.dummy_attribute
print('p.dummy_attribute:', res1)


# Handling Unknown Method Invocations

# The __getattr__() method is also invoked if an unknown method is called.
# For example, if we call the method dummy_method() on a Student object then
# an error is raised (in fact this is again an AttributeError). However, if we
# define a __getattr__() method we can return a reference to a method to use as a default

class Student2:
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

    # Method called if attribute is unknown
    def __getattr__(self, attribute):
        print('__getattr__: ', attribute)
        return self.my_default

    def my_default(self):
        return 'default'


student = Student2('John')
res2 = student.dummy_method()
print('student.dummy_method():', res2)


# Intercepting Attribute Lookup

class Student3:
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

    # Method called if attribute is unknown
    def __getattr__(self, attribute):
        print('__getattr__:', attribute)
        return 'default'
    
    # Method will always be called when an attribute
    # is accessed, will only called __getattr__ if it
    # does so explicitly or if an AttributeError is raised
    def __getattribute__(self, name):
        print('__getattribute__():', name)
        return object.__getattribute__(self, name)

    def my_default(self):
        return 'default'

# It is also possible to always intercept attribute lookups using the dot nation (e.g.
# student.name) by implementing the __getattribute__() method. This
#  method will always be called instead of looking the attribute up in the objects
#  dictionary. The __getattr__() method will only be called if an
#  AttributeError is raised or the __getattribute__() method explicitly
#  calls the __getattr__() method.
#  The __getattribute__() method should therefore return an attribute value
#  (which may be a default value) or raise an AttributeError if appropriate.
#  It is important to avoid implementing code that will recursively call itself (for
#  example calling self.name within __getattribute__() will result in a
#  recursive call back to __getattribute__()!). To avoid this the implementation of the method should either access the __dict__ directory or call the base
#  classes __getattribute__() method.
#  An example is given below of a simple __getattribute__() method that
#  logs the call to a method and then passes the invocation onto the base class implementation:

student = Student3('Leon')
print('student.name:', student.name) # instance lookup
res1 = student.dummy_attribute # invoke missing attribute
print('student.dummy_attribute:', res1)


# Intercepting Setting an Attribute

# It is also possible to intercept object/instance attribute assignment when the dot
# notation (e.g. student.name = 'Bob') is being used. This can be done by
# implementing the __setattr__() method. This method is invoked instead of the assignment.
# The __setattr() method can perform any action required including storing
# the value supplied. However, to do this it should either insert the value directly into the
# objects dictionary (e.g. student.__dict__['name'] = 'Bob') or preferably
# call the base class __setattr__() method, for example object.__
# setattr__(self, name, value) as shown below for the Student class:

class Student0:
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

    # Method will always be called when an attribute is set
    def __setattr__(self, name, value):
        print('__setattr__:', name, value)
        object.__setattr__(self, name, value)

student = Student('John')
student.name = 'Bob'
print('student.name:', student.name) # instance lookup

# There are a few things to note about this output:
# • Firstly the assignment of the Student’s name within the __init__() method
# also invokes the __setattr__() method.
# • Secondly, the assignment to the class variable count does not invoke the
# __setattr__() method.
# • Thirdly the student.name assignment does of course invoke the
# __setattr__() method.

print(student.__dict__)
print(Student.__dict__)
