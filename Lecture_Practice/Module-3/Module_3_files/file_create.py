'''open('test.txt', 'x') # x - mode for file creating

open('newfile.txt','w') # w - mode for file creating + write

open ('hello.txt', 'a') # a - mode for file creating + append'''

#----------------ppt example--------------
# file demo

file = open("test.txt","w")
file.write("Hello\n")
file.write("Welcome to file management program")
file.close
file = open("test.txt","r")
str=file.readline()
print(str)
a=file.tell()
print(a)
str=file.read()
print(str)