# Write a Python program to get a single string from two given strings, 
   # separated by a space and swap the first two characters of each string.

str1 = input("Please Enter First String : ")
str2 = input("Please Enter Second String : ")

x = str2[:2] + str1[2:]
y = str1[:2] + str2[2:]
 
print("Your first has become :- ",x)
print("Your second has become :- ",y)