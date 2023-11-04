# Write a Python program to read a file line by line store it into a variable.

file=open("python.txt","r")
data = file.readlines()
print(data)
file.close()