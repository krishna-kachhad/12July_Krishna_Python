# Write a Python program to map two lists into a dictionary.

#----------------using zip() function------------------------

students = ['Smith', 'John', 'Priska', 'Abhi']
marks = [89, 53, 92, 86]

students_dict = dict(zip(students, marks))
print(students_dict)

#----------------------user input and zip()function---------------

keys=[]
values=[]
n=int(input("Enter number of elements for dictionary:"))
print("For keys:")
for x in range(0,n):
    element=input("Enter element" + str(x+1) + ":")
    keys.append(element)

print("For values:")
for x in range(0,n):
    element=input("Enter element" + str(x+1) + ":")
    values.append(element)

d=dict(zip(keys,values))
print("The dictionary is:",d)
