# Write a Python program to get the Factorial number of given number.

'''The factorial of a number is the product of all the integers from 1 to that number. For example, the factorial of 6 is 1*2*3*4*5*6 = 720
Factorial is not defined for negative numbers, and the factorial of zero is one, 0! = 1.'''

#------------------------Using for loop-----------------------------------

n=int(input("Enter input number : "))

fact = 1
if n < 0:
    print ("Factorial does not exist for negative numbers")
elif n == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,n+1):
        fact = fact * i
    print("The factorial is",fact)


#---------------------------Using while loop------------------------------
n = int(input("Enter input number : "))
 
fact = 1
if n < 0:
    print("Factorial does not exist for negative numbers")
elif n == 0:
    print("The factorial of 0 is 1")
else:
  while(n > 0):
        fact = fact * n
        n = n - 1
  print("The factorial is",fact)