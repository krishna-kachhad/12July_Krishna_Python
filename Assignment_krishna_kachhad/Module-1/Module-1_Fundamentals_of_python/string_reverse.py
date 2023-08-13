# Write a Python function to reverses a string if its length is a multiple of 4.
'''Using slicing'''

mystr = input("Enter your string: ")

if len(mystr) % 4 == 0:
    print(mystr[::-1])
else:
    print("can't reverse the string")