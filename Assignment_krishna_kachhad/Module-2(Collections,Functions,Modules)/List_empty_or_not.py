# Write a Python program to check a list is empty or not.

list = []

if list == []:  # Checking whether the list object is equal to []
   print('Empty list')
else:
   print('List is not empty',list)

#-------------------Using len function----------
lst = []

# Checking whether the list size is equal to 0
if lst.__len__() == 0:
   print('Empty list')
else:
   print('Not Empty list')
