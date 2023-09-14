# Write a Python program to find the length of a tuple.

Tuple =( 1, 0, 4, 2, 5, 6, 7, 5)
print(len(Tuple))

#------------------user input-----------------------------

tuple = ()
n = int(input("Enter the no of elements: "))
for i in range(n):
    x = input("Enter an elements: ")
    tuple = tuple + (x,)
print(tuple)
print(len(tuple))
