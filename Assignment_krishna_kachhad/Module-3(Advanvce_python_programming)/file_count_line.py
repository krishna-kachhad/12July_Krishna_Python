# Write a Python program to count the number of lines in a text file.

file=open("python.txt","r")
x=file.readlines()
print(len(x))
file.close()

#--------------------------------or------------------------------------

file=open("python.txt","r")
x=file.readlines()
a=0
for i in x:
    a=a+1
print(a)
file.close()