# Write a Python program to create a tuple with numbers.

#-------------------Using list of append method--------------
list = []
n = int(input("Enter the no of elements: "))
for i in range(n):
    x = input("Enter an elements: ")
    list.append(x)

print(tuple(list))


#-------------------Using tuple()-------------------------------

tuple = ()
n = int(input("Enter the no of elements: "))
for i in range(n):
    x = input("Enter an elements: ")
    tuple = tuple + (x,)
print(tuple)
