#Write python program that swap two number with temp variable and without temp variable.

#-----------------with temp variable--------------
a=int(input("Enter the number1: "))
b=int(input("Enter the number2: "))

temp=a
a=b
b=temp
print("value of a:", a)
print("value of b:", b)

#--------------without temp variable--------------
a=int(input("Enter the number1: "))
b=int(input("Enter the number2: "))

a,b=b,a
print("value of a:", a)
print("value of b:", b)