#simple input from the user
nm=input("enter your name:")
print("your name is", nm)

pi=input("enter value")
print("value is", pi)

#first way
a=int(input("enter A:"))#by default input consider string value, so we convert into int(input())
b=int(input("enter B:"))
print("sum of two no", a+b)

#second way
a=input("enter a:")
b=input("enter b:")
print("sum:", int(a)+int(b))