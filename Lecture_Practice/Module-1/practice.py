#1
age=int(input("enter your age "))

if age>=18:
    print("you are eligible for vote")

#2
k=int(input("enter a "))
c=int(input("enter b "))

if k>c:
    print("a is greater")
elif k<c:
    print("b is greater")
else:
    print("both are equal")

#find radius
r=int(input("enter radius "))
pi=3.14

print("area of circle", pi*r*r)

#while odd no
i=1

while i<=10:
    print(i)
    i+=2

#even no
i=2

while i<=10:
    print(i)
    i+=2

#table of fifth
n=5
i=1

while i<=10:
    print(n, '*', i, '=', n*i)#simple
    print("{}, *, {}, =, {} ".format(n, i, n*i))#using format
    print(f"{n} * {i} = {n*i}")#using format
    i+=1