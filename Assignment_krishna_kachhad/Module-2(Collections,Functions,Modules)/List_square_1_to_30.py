# Write a Python program to generate and print a list of first and last 5 elements 
   # where the values are square of numbers between 1 and 30

list = []

for i in range(1,31):
    list.append(i**2)
print(list[0:5])
print(list[-5:])

'''if we get first &last 5 elements in one list.......
a=list[:5]+list[-5:]
print(a)'''