'''
Created on 10 jun. 2020

@author: RSSpe
'''

# Referential Transparency
amount = 1 
def increment(num): 
    return num + amount

print(increment(5))
amount = 2
print(increment(5)) 
