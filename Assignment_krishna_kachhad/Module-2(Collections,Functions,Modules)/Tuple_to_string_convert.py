# Write a Python program to convert a tuple to a string.

tuple = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e')
str =  ''.join(tuple)
print(str)


#------------------function with return keyword------------------------
def convertTuple(tuple):
    str = ''.join(tuple)
    return str
 
tuple = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e')
print(convertTuple(tuple))
