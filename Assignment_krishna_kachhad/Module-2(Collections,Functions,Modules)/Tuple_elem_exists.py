# Write a Python program to check whether an element exists within a tuple.

tuplex = ("p", "y", "t", "h", "o", "n")
print("p" in tuplex)
print(5 in tuplex)


#-------------------Using in operator-----------------------------

numTuple = (4, 6, 8, 11, 22, 43, 58, 99, 16)
print("Tuple Items = ", numTuple)

number = int(input("Enter Tuple Item to Find = "))

result = number in numTuple
print(result)