'''
Created on 11 jun. 2020

@author: RSSpe
'''
# Static method

class Primero: 
    @staticmethod 
    def static_function(): 
        print("4")
        
class Segundo(Primero):
    pass
        
Segundo.static_function()
