#-------------------single student data---------------------
id = input("Enter no: ")
name = input("Enter name: ")

fl = open("newfile.txt", "a") #In file using append previous data is not removed. previous data also store in file

fl.write(id)
fl.write(name)


#----------------------user input multiple student data---------------
fl=open('newfile.txt','a')
n = int(input("Enter the no of students: "))

for i in range(n):
    id = input("Enter Id: ")
    name = input("Enter Name: ")

    fl.write(f'ID: {id} Name: {name}\n')


