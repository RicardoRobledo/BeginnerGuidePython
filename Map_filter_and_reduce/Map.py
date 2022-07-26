'''
Created on 2 jul. 2020

@author: RSSpe
'''

# The function signature of map is
# map(function, iterable, ...)

data = [1, 3, 5, 2, 7, 4, 10]
print('data:', data)
# Apply the lambda function to each element in the list
# using the map function
d1 = list(map(lambda i: i + 1, data))
print('d1:', d1)
def add_one(i):
    return i + 1
# Apply the add_one function to each element in the
# list using the map function
d2 = list(map(add_one, data))
print('d2:', d2)
