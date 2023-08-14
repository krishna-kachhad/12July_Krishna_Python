# Write a Python program to count the number of characters (character frequency) in a string

string = input("Enter the string: ")

for i in string:
    frequency = string.count(i)
    print(str(i) + ": " + str(frequency), end=", ")
    

#----------------Using collection---------------
from collections import Counter
string = input("Enter the string: ")

output = Counter(string)

print(output)