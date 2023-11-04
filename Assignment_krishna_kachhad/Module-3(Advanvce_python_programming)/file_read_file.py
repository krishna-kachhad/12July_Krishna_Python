# Write a Python program to read an entire text file.

#-----------create file & write in file------------------
'''file = open("python.txt","w")
file.write("Hello\n")
file.write("Welcome to python file management\n")
file.write("Python has inbuilt functions to read a text file\n")
file.write("We can read files in three different ways.\n")
file.close()'''



#---------------------now read an entire file------------------
file=open("python.txt","r")
print(file.read())
file.close()