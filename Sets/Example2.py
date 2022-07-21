'''
Created on 27 jun. 2020

@author: RSSpe
'''

# The Set container also supports set like operations such as (|) union, intersection (&),
# difference (−) and symmetric difference (^). These are based on simple Set theory

programming_languages = {'Kotlin', 'Arduino', 'Java', 'Python'}
programming_languages2 = {'Kotlin', 'Python', 'Javascript', 'SQL'}

print(programming_languages)
print(programming_languages2)

print('Union:', programming_languages | programming_languages2)
print('Intersection:', programming_languages & programming_languages2)
print('Difference:', programming_languages - programming_languages2)
print('Symmetric Difference:', programming_languages ^ programming_languages2)


# Set methods
# Method   |   Description
# add()   |   Adds an element to the set
# clear()   |   Removes all the elements from the set
# copy()   |   Returns a copy of the set
# difference()   |   Returns a set containing the difference between two or more sets
# difference_update()   |   Removes the items in this set that are also included in another, specified set
# discard()   |   Remove the specified item
# intersection()   |   Returns a set, that is the intersection of two other sets
# intersection_update()  |   Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()   |   Returns whether two sets have a intersection or not
# issubset()   |   Returns whether another set contains this set or not
# issuperset()  |   Returns whether this set contains another set or not
# pop()   |   Removes an element from the set
# remove()   |   Removes the specified element
# symmetric_difference()   |   Returns a set with the symmetric differences of two sets
# symmetric_difference_update()  |   inserts the symmetric differences from this set and another
# union()   |   Return a set containing the union of sets
# update()   |   Update the set with the union of this set and others
