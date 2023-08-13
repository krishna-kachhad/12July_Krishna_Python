# Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user.
'''A number is even if division by 2 gives a remainder of 0. If the remainder is 1, it is an odd number.'''

num=int(input("Enter the no: "))

if num % 2 == 0:
    print ("This is even no")
else:
    print ("This is odd no")
