# WAP to print table from given number.(using only for loop).......e.g.8 * 1 = 8

'''n=int(input("Enter the number: "))

for i in range(1,n):

    print(f"{n} * {i} = {n*i}")#using format
    i=i+1'''

# WAP to print even and odd no up to 100 nos

'''for i in range(1,10,2):
    
    for j in range(2,10,2):
        print(f"{i}  {j}")

 
for x in range(0,12):
    if x%2==0:
        print(x,end="    ")
    else:
        print(x)'''

n=int(input("enter n"))
for i in range(n,2):
    print(i)
        
 # WAP to print employee information(id,name,address) with get input from user   
emp=[]

n=int(input("Enter number of employee:"))


for i in range(n):
    x1=input("Enter emp id:")
    x2=input("Enter emp name:")
    x3=input("Enter emp salary:")
    a=[x1, x2, x3]
    emp.append(a)
for b in emp:
    print(b)
    