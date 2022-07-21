'''
Created on 28 jun. 2020

@author: RSSpe
'''

cities = {'Wales': 'Cardiff',
          'England': 'London',
          'Scotland': 'Edinburgh',
          'Northern Ireland': 'Belfast',
          'Ireland': 'Dublin'}

print(cities)

# The dict() function can be used to create a new dictionary object from an iterable or a sequence of key:value pairs
# dict(**kwarg)
# dict(mapping, **kwarg)
# dict(iterable, **kwarg)

# The first option takes a sequence of key:value pairs.
# • The second takes a mapping and (optionally) a sequence of key:value pairs.
# • The third version takes an iterable of key:value pairs and an optional sequence
# of key:value pairs.
# Some examples are given below for reference:

# note keys are not strings
dict1 = dict(uk='London', ireland='Dublin', france='Paris')
print('dict1:', dict1)
# key value pairs are tuples
dict2 = dict([('uk', 'London'), ('ireland', 'Dublin'), ('france', 'Paris')])
print('dict2:', dict2)
# key value pairs are lists
dict3 = dict((['uk', 'London'], ['ireland', 'Dublin'], ['france', 'Paris']))
print('dict3:', dict3)

print('cities[Wales]:', cities['Wales'])
print('cities.get(Ireland):', cities.get('Ireland'))

cities['France'] = 'Paris'

cities['Wales'] = 'Swansea'
print(cities)

# An entry into the dictionary can be removed using one of the methods pop() or
# popitem() method or the del keyword

# The pop(<key>) method removes the entry with the specified key. This
# method returns the value of the key being deleted. If the key is not present then a
# default value (if it has been set using setdefault()) will be returned. If no
# default value has been set an error will be generated.
# • The popitem() method removes the last inserted item in the dictionary
# (although prior to Python 3.7 a random item in the dictionary was deleted
# instead!). The key:value pair being deleted is returned from the method.
# • The del keyword removes the entry with the specified key from the dictionary.
# This keyword just deletes the item; it does not return the associated value. It is
# potentially more efficient than pop(<key>)

cities = {'Wales': 'Cardiff', 'England': 'London', 'Scotland': 'Edinburgh', 'Northern Ireland': 'Belfast', 'Ireland': 'Dublin'}
print(cities)
cities.popitem() # Deletes 'Ireland' entry
print(cities)
cities.pop('Northern Ireland')
print(cities)
del cities['Scotland']
print(cities)

# In addition the clear() method empties the dictionary of all entries

cities = {'Wales': 'Cardiff', 'England': 'London', 'Scotland': 'Edinburgh', 'Northern Ireland': 'Belfast', 'Ireland': 'Dublin'}
print(cities)
cities.clear()
print(cities)

# Note that the empty dictionary is represented by the '{}' above which as the
# empty set was represented as set()

new_cities = {'Wales': 'Cardiff', 'England': 'London', 'Scotland': 'Edinburgh', 'Northern Ireland': 'Belfast', 'Ireland': 'Dublin'}

for country in new_cities:
    print(country, end=', ')
    print(new_cities[country])

# If you want to iterate over all the values directly, you can do so using the
# values() method. This returns a collection of all the values, which of course you
# can then iterate over

for e in new_cities.values():
    print(e)

# There are three methods that allow you to obtain a view onto the contents of a
# dictionary, these are values(), keys() and items().
# • The values() method returns a view onto the dictionary’s values.
# • The keys() method returns a view onto a dictionary’s keys.
# • The items() method returns a view onto the dictionary’s items ((key, value) pairs).
# A view provides a dynamic window onto the dictionary’s entries, which means
# that when the dictionary changes, the view reflects these changes.
# The following code iuses the cities dictionaries with these three methods:

print(new_cities.values())
print(new_cities.keys())
print(new_cities.items())

# You can check to see if a key is a member of a dictionary using the in syntax (and
# that it is not in a dictionary using the not in syntax)
print('Wales' in cities)
print('France' not in cities)

print(len(new_cities))

seasons = {'Spring': ('Mar', 'Apr', 'May'),
           'Summer': ('June', 'July', 'August'),
           'Autumn': ('September', 'October', 'November'),
           'Winter': ('December', 'January', 'February')}

print(seasons['Spring'])
print(seasons['Spring'][1])

# functions and how they are used in containers such as Dictionary.
# Method   |   Description
# clear()   |   Removes all the elements from the dictionary
# copy()   |   Returns a copy of the dictionary
# fromkeys()   |   Returns a dictionary with the specified keys and values
# get()   |   Returns the value of the specified key
# items()   |   Returns a list containing the tuple for each key value pair
# keys()   |   Returns a list containing the dictionary’s keys
# pop()   |   Removes the element with the specified key
# popitem()   |   Removes the last inserted key-value pair
# setdefault()   |   Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()   |   Updates the dictionary with the specified key-value pairs
# values()   |   Returns a list of all the values in the dictionary

class Persona:
    def __hash__(self):
        print("hash")
    
    def __eq__(self):
        print("eq")

cities2 = {'Wales': 'Cardiff',
          'England': 'London',
          'Scotland': 'Edinburgh',
          'Northern Ireland': 'Belfast',
          'Ireland': 'Dublin'}


print('key.__hash__():', 'England'.__hash__())
print("key.__eq__('England'):", 'England'.__eq__('England'))

# Python has two rules associated with these methods:
# • If two objects are equal, then their hashes should be equal.
# • In order for an object to be hashable, it must be immutable.
# It also has two properties associated with the hashcodes of an object that should be adhered to:
# • If two objects have the same hash, then they are likely to be the same object.
# • The hash of an object should be cheap to compute.
# Why do you need to care about these methods?
# For built in type you do not need to worry; however for user defined c lasses/
# types then if these types are to be used as keys within a dictionary then you should
# consider implementing these methods.
# This is because a Dictionary uses
# • the hashing method to manage how values are organised and
# • the equals method to check to see if a key is already present in the dictionary.
# As an aside if you want to make a class something that cannot be used as a key
# in a dictionary, that is it is not hashable, then you can define this by setting the
# __hash__() method to None.

class NotHashableThing(object):
    __hash__ = None


# print(NotHashableThing.__hash__())    Error

