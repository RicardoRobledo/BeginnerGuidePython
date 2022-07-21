'''
Created on 1 jul. 2020

@author: RSSpe
'''

# Coroutines
# however there is a fundamental difference between Generators and Coroutines:
# • generators are data producers
# • coroutines are data consumers

# The send() function is used to send values to a coroutine

# Part of the confusion between generators and coroutines is that the yield
# keyword is reused within a coroutine; it is used within a coroutine to cause the
# coroutine to wait until a value has been sent. It will then supply this value to the
# coroutine.
# It is also necessary to prime a Coroutine using with next() or send(None)
# functions. This advances the Coroutine to the call to yield where it will then wait
# until a value is sent to it.
# A coroutine may continue forever unless close() is sent to it. It is possible to
# pick up on the coroutine being closed by catching the GeneratorExit exception; you can then trigger some shut down behaviour if required.

def grep(pattern):
    print('Looking for', pattern)
    try:
        while True:
            line = (yield)
            if pattern in line:
                print(line)
    except GeneratorExit:
        print('Exiting the Co-routine') 

# This coroutine will wait for input data; when data is sent to the coroutine, then
# that data will be assigned to the line variable. It will then check to see if the
# pattern used to initialise the coroutine function is present in the line; if it is it will
# print the line; it will then loop and wait for the next data item to be sent to the
# coroutine. If while it is waiting the coroutine is closed, then it will catch the
# GeneratorExit exception and print out a suitable message

# The grep() coroutine is used below, notice that the coroutine function returns
# a coroutine object that can be used to submit data

print('Starting')
# Initialise the coroutine
g = grep('Python')
# prime the coroutine
next(g)
# Send data to the coroutine
g.send('Java is cool')
g.send('Kotlin is cool')
g.send('Python is cool')
# now close the coroutine
g.close()
