'''
Created on 1 jul. 2020

@author: RSSpe
'''

# The syntax of the filter() function is
# filter(function, iterable)

data = [1, 3, 5, 2, 7, 4, 10]
print('data:', data)
# Filter for even numbers using a lambda function
d1 = list(filter(lambda i: i % 2 == 0, data))
print('d1:', d1)
def is_even(i):
    return i % 2 == 0
# Filter for even numbers using a named function
d2 = list(filter(is_even, data))
print('d2:', d2)


# ---------------------------------------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f'Person({self.name}, {self.age})'


data = [Person('Alun', 54), Person('Niki', 21), Person('Megan', 19)]

for p in data:
    print(p, end=', ')

print('\n---------------------------')
# Use a lambda to filter out People over 21
d3 = list(filter(lambda p: p.age <= 21, data))
for p in d3:
    print(p, end=', ')