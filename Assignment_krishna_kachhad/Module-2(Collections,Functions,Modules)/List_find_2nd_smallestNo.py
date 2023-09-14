# Write a Python program to find the second smallest number in a list.

list = [] 
n = int(input("Enter the number of elements: "))
for i in range(1, n+1): 
    elem = int(input("Enter the elements: ")) 
    list.append(elem) 
list.sort() 

print("The sorted list: ", list) 
print("The second smallest value of this list: ",list[1])