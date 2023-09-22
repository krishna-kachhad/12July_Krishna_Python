fl = open("newfile.txt","r")

#print(fl.read())
#print(fl.readline()) #only read first line
#print(fl.readlines()) #return data in list[]
#print(fl.readlines()[-1]) #read last line in---- we can also use slicing for read specific lines

#------------------------------------------------
n=1
for i in fl:
    #print(i)
    print(f"Line:{n} = {i}")
    n+=1