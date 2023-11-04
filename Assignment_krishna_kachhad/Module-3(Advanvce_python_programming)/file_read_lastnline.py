# Write a Python program to read last n lines of a file.

file=open("python.txt","r")
print(file.readlines()[-1])
file.close()