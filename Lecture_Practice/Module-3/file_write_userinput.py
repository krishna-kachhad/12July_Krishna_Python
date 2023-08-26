fl = open("test.txt", "w") # using write the previous data is deleted and add only last data

id = input("Enter no: ")
name = input("Enter name: ")

fl.write(id)
fl.write(name)