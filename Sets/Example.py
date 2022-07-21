'''
Created on 27 jun. 2020

@author: RSSpe
'''

# Set
programming_languages = {'Kotlin', 'Arduino', 'Java', 'Python', 'Kotlin', 'Python'}

print(programming_languages)


# Convert a list in a set
# It is not possible to change the items already in a Set
set_list = ['Kotlin', 'Arduino', 'Java', 'Python']

new_set = set(set_list)

print(new_set)



# Checking element
print('Python' in set_list)


# Iterating elements of a Set
for language in new_set:
    print(language)


# Add elements in a set
new_set.add("Javascript")

print(new_set)


# Add more than one element to a Set
new_set.update(['C#', 'Go', 'SQL'])

print(new_set)


#Max and Min values in a Set
#Alphabetic order
print(max(new_set))
print(min(new_set))
#Number order
set_with_numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(max(set_with_numbers))
print(min(set_with_numbers))


#Removing an item with remove() and discard()
# The remove() function removes a single item from a Set but generates an error if
# that item was not initialling the set. The remove() function also removes a single
# item from a set but does not throw an error if it was not initially present in the set
new_set.remove('C#')
new_set.discard('Go')

print(new_set)


# There is also a method pop() that can be used to remove an item (and return
# that item as a result of running the method); however it removes the last item in the
# Set (although as a set is unordered you will not know which item that will be)
new_set.clear()
print(new_set)
# The method clear() is used to remove all elements from a Set


# It is possible to hold any immutable object within a set This means that a set can
# contain a reference to a Tuple (as that is immutable)
s1 = {(1, 2, 3)}
print(s1)


# we cannot nest Lists or other Sets within a Set as these are not immutable types
# Can't have the following
'''s2 = { {1, 2, 3} }
print(s2)
s3 = { [1, 2, 3] }
print(s3)'''
# However we can use Frozensets and nest these within sets. A Frozenset
# is exactly like a Set except that it is immutable (it cannot be modified) and thus it
# can be nested within a Set
# Need to convert sets and lists into frozensets
s2 = { frozenset({1, 2, 3}) }
print(s2)
s3 = { frozenset([1, 2, 3]) }
print(s3)

