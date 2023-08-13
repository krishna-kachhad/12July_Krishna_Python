# Write a Python program to get the Fibonacci series of given range.

'''A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8....The first two terms are 0 and 1. '''

num = int(input("Enter number: "))
n1=0
n2=1
print("Fibonacci Series:", n1, n2, end=" ")

for i in range(2,num):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3, end=" ")