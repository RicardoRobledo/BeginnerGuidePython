'''
Created on 2 jul. 2020

@author: RSSpe
'''

# The reduce() function is the last higher order function that can be used with
# collections of data that we will look at.
# The reduce() function applies a function to an iterable and combines the
# result returned for each element together into a single result.
# This function was part of the core Python 2 language but was not included into
# the core of Python 3. This is partly because Guido van Rossum believed (probably
# correctly) that the applicability of reduce is quite limited, but where it is useful it
# is very useful. Although it has to be said that some developers try and shoe horn
# reduce() into situations that just make the implementation very hard to understand—remember always aim to keep it simple.
# To use reduce() in Python 3 you need to import it from the functoolsmodule.
# One point that is sometimes misunderstood with reduce() is that the function passed
# into reduce takes two parameters, which are the previous result and the next value in the
# sequence; it then returns the result of applying some operation to these parameters.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f'Person({self.name}, {self.age})'

# The signature of the functools.reduce function is:
# functools.reduce(function, iterable[, initializer])

from functools import reduce

data = [1, 3, 5, 2, 7, 4, 10]
result = reduce(lambda total, value: total + value, data)
print(result)

# ----------------------------------------------

# Although it might appear that reduce() is only useful for numbers such as
# integers; it can be used with other types as well. For example, let us assume that we
# want to calculate the average age for a list of people, we could use reduce to add
# together all the ages and then divide by the length of the data list we are processing

data = [Person('John', 54), Person('Phoebe', 21), Person('Adam', 19)]
total_age = reduce(lambda running_total, person: running_total + person.age, data, 0)
average_age = total_age // len(data)
print('Average age:', average_age)

# In this code example, we have a data list of three people. We then use the reduce
# function to apply a lambda to the data list. The lambda takes a running_total
# and adds a person’s age to that total. The value zero is used to initialise this running total
# When the lambda is applied to the data list, we will add 54, 21 and 19 together.
# We then divide the final result returned by the length of the data list (3) using the
# // operator which will use floor() division to return a whole integer (rather than a
# real number such as 3.11)
