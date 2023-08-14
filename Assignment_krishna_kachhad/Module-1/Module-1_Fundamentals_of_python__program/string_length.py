# Write a Python program to calculate the length of a string.
str=input("Enter the string: ")

print("Length of the input string is:", len(str))


#-------------without using len()function-------------------
str = input("Enter a string: ")

# counter variable to count the character in a string
counter = 0
for s in str:
      counter = counter+1
print("Length of the input string is:", counter)