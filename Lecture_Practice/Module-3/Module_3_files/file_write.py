fl = open('hello.txt', 'w') #we take fl as a object

fl.write("hello! how are you....")

if fl.writable():
    print("yes")
else:
    print("no")