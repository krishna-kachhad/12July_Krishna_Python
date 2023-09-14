# Write a Python program to reverse a tuple.

#---------------using built in reversed() function----------------------
list = []
n = int(input("Enter the no of elements: "))
for i in range(n):
    x = input("Enter elements: ")
    list.append(x)
tuplex = tuple(list)
print("Original tuple: " ,tuplex)

rev_tuple = reversed(tuplex)
print(tuple(rev_tuple))


#---------------------static---------------------------
x = (5, 10, 15, 20)
# Reversed the tuple
y = reversed(x)
print(tuple(y))


#------------------------using slicing method--------------
def Reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup   
# Driver Code
tuples = ('z','a','d','f','g','e','e','k')
print(Reverse(tuples))