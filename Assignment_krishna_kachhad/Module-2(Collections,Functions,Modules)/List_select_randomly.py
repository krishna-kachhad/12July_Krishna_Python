# Write a Python program to select an item randomly from a list.

#---------------Using random.choice() function-------------
import random

my_list = [1, 'a', 32, 'c', 'd', 31, 'xyz']
print("Original list is : " , my_list)
print(random.choice(my_list))