# Write a Python program to read a file line by line and store it into a list.

file=open("python.txt","r")
print(file.readlines())
file.close()

#-----------------------------------------------------------------------------

l1=[]
file=open("python.txt","r")
for i in file:
    l1.append(file.readlines())
print(l1)