'''
Created on 29 jun. 2020

@author: RSSpe
'''

def logger(func):
    def inner():
        print('calling ', func.__name__)
        func() 
        print('called ', func.__name__)

    return inner

@logger
def target():
    print('In target function')


# t1 = logger(target)
# t1()

target()

#-----------------------------------

def logger2(func):
    def inner(x, y):
        print('calling ', func.__name__, 'with', x, 'and', y)
        func(x, y)
        print('returned from ', func.__name__)

    return inner

@logger2
def my_func(x, y):
    print(x, y)


my_func(4, 5)

# Stacked decorators

# Define the decorator functions
def make_bold(fn):
    def makebold_wrapped():
        return "<b>" + fn() + "</b>"
    return makebold_wrapped

def make_italic(fn):
    def makeitalic_wrapped():
        return "<i>" + fn() + "</i>"
    return makeitalic_wrapped

# Apply decorators to function hello
@make_bold
@make_italic
def hello():
    return 'hello world'


# Call function hello
print(hello())


# Decorators can also take parameters however the syntax for such decorators is a
# little different; there is essentially an extra layer of indirection. The decorator
# function takes one or more parameters and returns a function that can use the
# parameter and takes the callable object that is being wrapped. For example:

def register(active=True):
    def wrap(func):
        def wrapper():
            print('Calling ', func.__name__, ' decorator param', active)
            if active:
                func()
                print('Called ', func.__name__)
            else:
                print('Skipped ', func.__name__)
        return wrapper
    return wrap

@register()
def func1():
    print('func1')

@register(active=False)
def func2():
    print('func1')


func1()
print('-' * 10)
func2()


# In this example, the wrapped function will only be called if the active parameter
# is True. This is the default and so for func1() it is not necessary to specify the
# parameter (although note that it is now necessary to provide the round brackets).
# For func2() the @register decorator is defined with the active parameter set
# to False. This means that the wrapper function will not call the provided function.
# Note that the usage of the decorator only differs in the need to include the round
# brackets even if no parameters are being specified; even though there are now two
# inner functions defined within the register decorator


# Method Decorators

# It is also possible to decorate methods as well as functions (as they are also callable
# objects). However, it is important to remember that methods take the special
# parameter self as the first parameter which is used to reference the object that the
# method is being applied to. It is therefore necessary for the decorator to take this
# parameter into account; i.e. the inner wrapped function must take at least one
# parameter representing self:
# The pretty_print decorator defines an inner function that takes as its first (and
# in this case only) parameter the reference to the object (which by convention uses the
# parameter self). This is then passed into the actual method when it is called.
# The pretty_print decorator can now be used with any method that only
# takes the self parameter, for example

def pretty_print(method):
    def method_wrapper(self):
        return "<p>{0}</p>".format(method(self))
    return method_wrapper

class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def print_self(self):
        print('Person - ', self.name, ', ', self.age)

    @pretty_print
    def get_fullname(self):
        return self.name + " " + self.surname


a=Person("Sigmund", "Orbent", "Hero")
print(a.get_fullname())


# Methods with Parameters

def trace(method):
    def method_wrapper(self, x, y):
        print('Calling', method, 'with', x, y)
        method(self, x, y)
        print('Called', method, 'with', x, y)
    return method_wrapper


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    @trace
    def move_to(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return 'Point - ' + str(self.x) + ',' + str(self.y)


p = Point(1, 1)
print(p)
p.move_to(5, 5)
print(p)

def singleton(cls):
    print('In singleton for: ', cls)
    instance = None
    
    def get_instance():
        nonlocal instance
        if instance is None:
            instance = cls()
        return instance
    return get_instance


@singleton
class Service(object):
    def print_it(self):
        print(self)

@singleton
class Foo(object):
    pass


print('Starting')
s1 = Service()
print(s1)
s2 = Service()
print(s2)
f1 = Foo()
print(f1)
f2 = Foo()
print(f2)

# ----------------------------------

def logger3(func):
    print('In Logger')
        
    def inner():
        print('In inner calling ', func.__name__)
        func()
        print('In inner called ', func.__name__)
        print('Finishing Logger')
    return inner

@logger3
def print_it():
    print('Print It')


print('Start')
print_it()
print('Done')

# Built-in Decorators

# There are numerous built-in decorators in Python 3; some of which we have already
# seen such as @classmethod, @staticmethod and @property. We also saw
# some decorators when talking about abstract methods and properties. There are also
# decorators associated with unit testing and asynchronous operations

# FuncTools Wrap

# One issue with decorated functions may become apparent when debugging or
# trying to trace what is happening. The problem is that by default the attributes
# associated with the function being called are actually those of the inner function
# returned by the decorator function. That is the name, doc and module of the
# function are those of the function returned by the decorator. The name and
# documentation of the original, decorated function, have been lost

def logger0(func):
    def inner():
        print('calling', func.__name__)
        func()
        print('called', func.__name__)
    return inner

@logger0
def get_text(name):
    """returns some text"""
    return "Hello ",name


print('name:', get_text.__name__)
print('doc: ', get_text.__doc__)
print('module: ', get_text.__module__)

# ----------------------------------------------------
print("------------------------")
# Python has included the functools module which contains
# the functools.wraps decorator which can be used to overcome this problem.
# Wraps is a decorator for updating the attributes of the wrapping function(inner)
# to those of the original function (in this case get_text()). This is as simple as
# decorating the 'inner' function with @wraps(func).

from functools import wraps

def logger4(func):
    @wraps(func)
    def inner():
        print('calling ', func.__name__)
        func()
        print('called ', func.__name__)
    return inner

# The end result is that in the above example the name and doc are now updated
# to the name of the wrapped function and the documentation associated with that function

@logger4
def get_text2(name):
    """returns some text"""
    return "Hello ",name


print('name:', get_text2.__name__)
print('doc: ', get_text2.__doc__)
print('module: ', get_text2.__module__)
