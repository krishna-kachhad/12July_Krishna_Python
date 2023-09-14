# Write a Python program to convert a list of characters into a string.

str = ['p', 'y', 't', 'h', 'o', 'n']
str1 = ''.join(str)
print(str1)

#-----------------------Using function--------------------
def convert(str):
    str1 = ""
    return(str1.join(str))

str = ['p', 'y', 't', 'h', 'o', 'n']
print(convert(str))