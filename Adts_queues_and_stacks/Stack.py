'''
Created on 2 jul. 2020

@author: RSSpe
'''

# The basic facilities provided by a Stack include:
# • Stack creation.
# • Add an element to the top of the stack (known as pushing onto the stack).
# • Remove an element from the top of the stack (known as popping from the stack).
# • Find out the length of the stack.
# • Check to see if the stack is empty.
# • Stacks can be of fixed size or a variable (growable) stack.

class Queue:
    def __init__(self):
        self._list = [] # initial internal data

    def push(self, element):
        self._list.append(element)

    def pop(self):
        return self._list.pop(0)

    def __len__(self):
        """ Supports the len protocol """
        return len(self._list)

    def is_empty(self):
        return self.__len__() == 0

    def peek(self):
        return self._list[0]

    def __str__(self):
        return 'Queue: ' + str(self._list)


stack = [] # create an empty stack
stack.append('task1')
stack.append('task2')
stack.append('task3')
print('stack:', stack)
top_element = stack.pop()
print('top_element:', top_element)
print('stack:', stack)

# This certainly works although when we print out the stack it does not make it
# clear that ‘task3’ is at the front of the stack.
# In addition, as when using the List as a queue ADT it is still possible to apply
# any of the other methods defined on a List to this stack and thus we can still write
# stack.pop(0) which would remove the very first element added to the stack.
# We could therefore implement a Stack class to wrap the list and provide
# suitable stack like behaviour as we did for the Queue class.
