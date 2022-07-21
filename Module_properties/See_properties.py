'''
Created on 23 jun. 2020

@author: RSSpe
'''

import Module_Example
# These properties are considered special as they all start, and end, with a double
# underbar ('__'). These are:
# • __name__ the name of the module
# • __doc__ the doctoring for the module
# • __ﬁle__ the ﬁle in which the module was deﬁned.

print(Module_Example.__name__)
print(Module_Example.__doc__)
print(Module_Example.__file__)
print("All the properties of modules:", dir(Module_Example))


# Standart modules
import sys


print('sys.version: ', sys.version)
print('sys.maxsize: ', sys.maxsize)
print('sys.path: ', sys.path)
print('sys.platform: ', sys.platform)
