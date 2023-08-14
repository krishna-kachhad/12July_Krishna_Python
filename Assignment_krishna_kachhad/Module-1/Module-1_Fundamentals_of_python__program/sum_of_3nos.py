# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

n1=int(input("Enter first value:"))
n2=int(input("Enter second value:"))
n3=int(input("Enter third value:"))
sum=n1+n2+n3

if n1 == n2 or n2 == n3 or n3 == n1:
    print("Sum is zero...")
else:
    print("Sum of three numbers are ",sum)