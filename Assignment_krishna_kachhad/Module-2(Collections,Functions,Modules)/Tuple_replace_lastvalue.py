# Write a Python program to replace last value of tuples in a list.

#---------Using list comprehension & slicing operator--------
l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print([t[:-1] + (100,) for t in l])


#------------------user input-------------------

list = []
n = int(input("Enter the no of elements: "))
for i in range(n):
    x = input("Enter elements: ")
    list.append(x)
print(list)
tuplex = tuple(list)
              #--replace last element using slicing
replace_tup = tuplex[:-1] + (90,)
print(replace_tup)