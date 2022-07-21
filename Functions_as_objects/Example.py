'''
Created on 9 jun. 2020

@author: RSSpe
'''
# Function as object
def get_msg(): 
    return 'Hello Python World!'

message = get_msg
print(message)
print(type(get_msg))

# ------------------------------------

def get_some_other_msg(): 
    return 'Some other message!!!' 

get_msg = get_some_other_msg

another_reference = get_msg
print(another_reference())

print(get_msg())
print(get_msg)
print(another_reference())
print("Los 2 tienen la misma direccion en memoria:", get_msg is another_reference)
