'''
Created on 30 jun. 2020

@author: RSSpe
'''

# Iteration

# To be an iterable type; it is necessary to implement the __iter__() method
# (which is the only method in the Iterable protocol)


# Iterators

# An iterator is an object that will return a sequence of values. Iterators may be finite
# in length or infinite (although many container-oriented iterators provide a fixed set of values).
# The iterator protocol specifies the __next__() method. This method is
# expected to return the next item in the sequence to return or to raise the
# StopIteration exception. This is used to indicate that the iterator has finished supplying values.

# The Iteration Related Methods
# To summarise then we have
# • __iter__() from the Iterable protocol which is used to return the iterator object,
# • __next__() from the Iterator protocol which is used to obtain the next value
# in a sequence of values.
# Any data type can be both an Iterable and an Iterator; but that is not required. An
# Iterable could return a different object that will be used to implement the iterator or
# it can return itself as the iterator—it’s the designers choice

class Evens(object):
    def __init__(self, limit):
        self.limit = limit
        self.val = 0

    # Makes this class iterable
    def __iter__(self):
        return self
    
    # Makes this class an iterator
    def __next__(self):
        if self.val > self.limit:
            raise StopIteration
        else:
            return_val = self.val
            self.val += 2
            return return_val


ev = Evens(10)
print(ev.__next__())
print(ev.__next__())
print(ev.__next__())
print(ev.__next__())
print(ev.__next__())
print(ev.__next__())


# Using the Evens2 Class with a for Loop

class Evens2(object):
    def __init__(self, limit):
        self.limit = limit
        self.val = 0

    # Makes this class iterable
    def __iter__(self):
        return self
    
    # Makes this class an iterator
    def __next__(self):
        if self.val > self.limit:
            raise StopIteration
        else:
            return_val = self.val
            self.val += 2
            return return_val
        
        
print('Start')
for i in Evens2(6):
    print(i, end=', ')
print('Done')

# This makes it look as if the Evens type is a built-in type as it can be used with
# an existing Python structure; however the for loop merely expects to be given an
# iterable; as such Evens is compatible with the for loop


# The Itertools Module

# The itertools module provides a number of useful functions that return iterators constructed in various ways. It can be used to provide an iterator over a
# selection of values from a data type that is iterable; it can be used to combine
# iterables together etc