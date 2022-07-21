'''
Created on 30 jun. 2020

@author: RSSpe
'''

# Monkey Patching

class Bag():
    def __init__(self):
        self.data = ['a', 'b', 'c']

    def __getitem__(self, pos):
        return self.data[pos]
    
    def get_length(self):
        return len(self.data)

    def __str__(self):
        return 'Bag(' + str(self.data) + ')'


b = Bag()
print(Bag.__dict__)
print(b.__dict__)
#print(len(b)) error

# Monkey patching
Bag.__len__ = b.get_length

# Now when we invoke
print(len(b))

# name
Bag.name = 'My Bag'
print(b.name)

b.name = 'Johns Bag'
print(b.name)
b2 = Bag()
print(b2.name)


#Thus each instance of the class Student will have its own name attribute
class Student:
    count = 0
    def __init__(self, name):
        self.name = name
        Student.count += 1

student = Student('John')
# Class attribute dictionary
print('Student.__dict__:', Student.__dict__)
# Instance / Object dictionary
print('student.__dict__:', student.__dict__) 

# To look up an attribute, Python does the following for class attributes:
# 1. Search the class Dictionary for an attribute
# 2. If the attribute is not found in step 1 then search the parent class(es) dictionaries
# For object attributes, Python first searches the instance dictionary and repeats the
# above steps, it thus performs these steps:
# 1. Search the object/instance dictionary
# 2. If the attribute was not found in step 1, then search the class Dictionary for an attribute
# 3. If the attribute is not found in step 2, then search the parent class(es) dictionaries

student = Student('John')
print('Student.count:', Student.count) # class lookup
print('student.name:', student.name) # instance lookup
print('student.count:', student.count) # lookup finds class attribute


# class lookup
print('Student.count:', Student.count)
print("Student.__dict__['count']:", Student.__dict__['count'])
# Instance / Object Lookup
print('student.name:', student.name)
print("student.__dict__['name']:", student.__dict__['name'])

# However, accessing attributes via the __dict__ does not trigger a search
# process; it is instead a direct lookup in the associated dictionary container
# Thus if you try to access a class variable via the
# objects __dict__ then you will get an error

# Attempt to look up class variable via object
#print('student.name:', student.name)
#print("student.__dict__['count']:", student.__dict__['count'])
