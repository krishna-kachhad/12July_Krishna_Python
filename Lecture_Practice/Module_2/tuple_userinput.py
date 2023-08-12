data=[]

n=int(input("Enetr no of elements: "))

for i in range(n):
    x=input("Enter an elements ")
    data.append(x)

print(tuple(data))

#---------------------------------------
#Convert list to tuple
listx = [5, 10, 7, 4, 15, 3]
print(listx)
#use the tuple() function built-in Python, passing as parameter the list
tuplex = tuple(listx)
print(tuplex)
