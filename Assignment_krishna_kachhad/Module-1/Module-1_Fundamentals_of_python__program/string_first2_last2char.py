# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
   #If the string length is less than 2, return instead of the empty string.

#------------------------Using if_else----------------------
string = input("Enter string:")

if len(string) < 2:
    print ("Return empty")
else:
    newString = "{}{}".format(string[0:2], string[-2:])
    print("New string: ", newString)


#------------------------Using function----------------------
def get_str(str):
    if len(str) < 2:
        return "------"
    return str[0:2] + str[-2:]

my_str=input("Enter string: ")

print("New modified string is:" ,get_str(my_str) )
    