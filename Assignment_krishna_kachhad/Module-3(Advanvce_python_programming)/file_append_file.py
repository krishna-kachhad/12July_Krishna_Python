# Write a Python program to append text to a file and display the text.

file=open("python.txt","a")
print(file.write("This is python library....\n"))



file=open("python.txt","r") #display the text
print(file.read())
file.close()