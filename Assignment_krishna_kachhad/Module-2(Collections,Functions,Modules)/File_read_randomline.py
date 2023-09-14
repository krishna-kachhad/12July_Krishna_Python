# Write a Python program to read a random line from a file.

#-----------------optional(create a file)---------------
file = open("file.txt", "w")
file.write("Hello\n")
file.write("Welcome to file\n")
file.write("choose any line randomly\n")
file.write("close the file")
file.close()

#----------------Read a random line-----------------------
import random
file = open('file.txt').read().splitlines()
myline =random.choice(file)
print(myline)
