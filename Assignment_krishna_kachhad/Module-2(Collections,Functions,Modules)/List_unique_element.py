# Write a Python function that takes a list and returns a new list with unique elements of the first list.

numbers = input("Enter Numbers: ")
list = []
for i in numbers:
   if i not in list: # (OR) if i in list == false
      list.append(i)
      
print(list)

#-------------using function----------------
def unique_list(numbers):
    unique = []
    for i in numbers :
        if i not in unique:
            unique.append(i)
    return unique

print(unique_list([1, 2, 3, 1, 2])) # output = [1,2,3]


#--------------------using set -----------------------
def unique_list(numbers):
   x=set(numbers)           #unique numbers in set
   y=list(x)                #convert set to list as you want your output in LIST.
   print(y)
unique_list([1,1,2,2,3,4])