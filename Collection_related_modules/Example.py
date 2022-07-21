'''
Created on 28 jun. 2020

@author: RSSpe
'''

# List comprehesion
# [ <expression> for item in iterable <if optional_condition> ]
list1 = [1, 2, 3, 4, 5,6]
print('list1:', list1)

list2 = [item + 1 for item in list1]
print('list2:', list2)

list3 = [item + 1 for item in list1 if item % 2 == 0]
print('list3:', list3)

# The Collections Module
# The collections module extends that basic features of the collection-oriented
# data types within Python with high performance container data types. It provides
# many useful containers such as:
# Name   |   Purpose
# namedtuple()   |   Factory function for creating tuple subclasses with named fields
# deque   |   List-like container with fast appends and pops on either end
# ChainMap   |   Dict-like class for creating a single view of multiple mappings
# Counter   |   Dict subclass for counting hashable objects
# OrderedDict   |   Dict subclass that remembers the order entries were added
# Defaultdict   |   Dict subclass that calls a factory function to supply missing values
# UserDict   |   Wrapper around dictionary objects for easier dict subclassing
# UserList   |   Wrapper around list objects for easier list subclassing
# UserString   |   Wrapper around string objects for easier string subclassing

# As this is not one of the default modules that are automatically loaded for you by
# Python; you will need to import the collection.
# As an example, we will use the Counter type to efficiently hold multiple
# copies of the same element. It is efficient because it only holds one copy of each
# element but keeps a count of the number of times that element has been added to the collection

import collections

fruit = collections.Counter(['apple', 'orange', 'pear', 'apple', 'orange', 'apple'])

print(fruit)
print(fruit['orange'])

# There are many uses of such a class, for example, it can be used to find out the
# most frequently used word in an essay; all you have to do is add each word in an
# essay to the Counter and then retrieve the word with the highest count. This can
# be done using the Counter class’s most_common() method. This method takes
# a parameter n that indicates how many of the most common elements should be
# returned. If n is ommitted (or None) then the method returns an ordered list of
# elements. Thus to obtain the most common fruit from the above Counter collection we can use:

print('fruit.most_common(1):', fruit.most_common(1))

fruit1 = collections.Counter(['apple', 'orange', 'pear',
'orange'])
fruit2 = collections.Counter(['banana', 'apple', 'apple'])
print('fruit1:', fruit1)
print('fruit2:', fruit2)
print('fruit1 + fruit2:', fruit1 + fruit2)
print('fruit1 - fruit2:', fruit1 - fruit2)
# Union (max(fruit1[n], fruit2[n])
print('fruit1 | fruit2:', fruit1 | fruit2)
# Intersection (min(fruit1[n], fruit2[n])

print('apple' in fruit)

fruit['apple'] = 1 # initialises the number of apples
fruit['apple'] =+ 1 # Adds one to the number of apples
fruit['apple'] =- 1 # Subtracts 1 from the number of apples 


# The Itertools Module

# The itertools module is another module that it is worth being familiar with.
# This module provides a number of useful functions that return iterators constructed in various ways

import itertools
# Connect two iterators together
r1 = list(itertools.chain([1, 2, 3], [2, 3, 4]))
print(r1)
# Create iterator with element repeated specified number of
# times (possibly infinite)
r2 = list(itertools.repeat('hello', 5))
print(r2)
# Create iterator with elements from first iterator starting
# where predicate function fails
values = [1, 3, 5, 7, 9, 3, 1]
r3 = list(itertools.dropwhile(lambda x: x < 5, values))
print(r3)
# Create iterator with elements from supplied iterator between
# the two indexes (use ‘None’ for second index to go to end)
r4 = list(itertools.islice(values, 3, 6))
print(r4)
