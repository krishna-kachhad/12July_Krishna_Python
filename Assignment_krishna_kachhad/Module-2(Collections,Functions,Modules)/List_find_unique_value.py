# Write a Python program to get unique values from a list.

lst = []
n = int(input("Enter no of elements: "))
for i in range(n):
    x=int(input("Enter elements: "))
    print(x)
    lst.append(x)
print("Original List : ",lst)
s = set(lst)
print(s)
new_list = list(s)
print("Unique Numbers : ",new_list)



#------------------Using list.append() function------------
list = [100, 75, 100, 20, 75, 12, 75, 25] 
unique_list = []
 
# traverse for all elements
for x in list:
    if x not in unique_list:
        unique_list.append(x)
print(unique_list)
      