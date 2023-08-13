# Write a Python program to count the number of characters (character frequency) in a string
string = "welcome to home"

for i in string:
    frequency = string.count(i)
    print(str(i) + ": " + str(frequency), end=", ")
    

#----------------Using collection---------------
from collections import Counter
string = "welcome to home"

output = Counter(string)

print(output)