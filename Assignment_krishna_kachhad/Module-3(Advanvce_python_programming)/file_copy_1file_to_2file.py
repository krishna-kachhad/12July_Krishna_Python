# Write a Python program to copy the contents of a file to another file.

file1 = open("python.txt", "r")
file2 = open("python_file.txt", "a")

for i in file1:
    file2.write(i)