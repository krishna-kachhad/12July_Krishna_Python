#set() declare like this..... otherwise it takes as a dictionary
myset=set() 

n=int(input("Enter number of elements:"))

for i in range(n):
    x=input("Enter an element:")
    myset.add(x)

print(myset)