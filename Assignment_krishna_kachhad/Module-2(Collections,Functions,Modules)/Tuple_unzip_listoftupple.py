# Write a Python program to unzip a list of tuples into individual lists.

# ------------------Using zip() and * operator------------
l = [(1,2), (3,4), (8,9)]
print(list(zip(*l))) #The * operator is used to unpack the list of tuples l into separate positional arguments. 


#-------------------Using lists and tuple() method------------------

test_list = [('Akshat', 1), ('Bro', 2), ('is', 3), ('Placed', 4)]
print("Original list is : " + str(test_list))
 
# Empty dictionary
res = []
a = []
b = []
 
for i in test_list:
    a.append(i[0])
    b.append(i[1])
 
res.append(tuple(a))
res.append(tuple(b))

# Printing modified list
print("Modified list is : " + str(res))