'''
Created on 2 jul. 2020

@author: RSSpe
'''

# Adts_queues_and_stacksThere are numerous variations on the basic queue operations but in essence all
# queues provide the following features:
# • Queue creation.
# • Add an element to the back of the queue (known as enqueuing).
# • Remove an element from the front of the queue (known as dequeuing).
# • Find out the length of the queue.
# • Check to see if the queue is empty.
# • Queues can be of fixed size or variable (growable) in size.

# Python List as a Queue
# The Python List container can be used as a queue using the existing operations
# such as append() and pop(), for example:

queue = [] # Create an empty queue
queue.append('task1')
print('initial queue:', queue)
queue.append('task2')
queue.append('task3')
print('queue after additions:', queue)

# Defining a Queue Class

class Queue:
    def __init__(self):
        self._list = [] # initial internal data

    def enqueue(self, element):
        self._list.append(element)

    def dequeue(self):
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


queue = Queue()
print('queue.is_empty():', queue.is_empty())
queue.enqueue('task1')
print('len(queue):', len(queue))
queue.enqueue('task2')
queue.enqueue('task3')
print('queue:', queue) 
print('queue.peek():', queue.peek())
print('queue.dequeue():', queue.dequeue())
print('queue:', queue)

# This provides a far more explicit and semantically more meaningful implementation of a Queue than the use of the raw List data structure.
# Of course, Python understands this and provides a queue container class in the
# collections module called deque. This implementation is optimised to be
# more efficient than the basic List which is not very efficient when it comes to
# popping elements from the front of the list
