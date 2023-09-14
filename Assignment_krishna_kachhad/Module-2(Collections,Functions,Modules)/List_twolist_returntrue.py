# Write a Python function that takes two lists and returns true if they have at least one common member.

#-----------------------static list------------------------

list1 = [1, 2, 3, 4, 55]
list2 = [2, 3, 90, 22]
 # using set
out = set(list1) & set(list2)
 # Checking condition
if out:
    print("True")
else :
    print("False")


#---------------------User input list------------------
    
list1 = [] #or a=list()
list2 = [] #or b=list()
n1 = int(input("Enter the size of list1: "))
for i in range(n1):
    k=input("Enter the element of list1: ")
    list1.append(k)
print(list1)

n2 = int(input("Enter the size of list2: "))
for i in range(n2):
    k=input("Enter the element of list2: ")
    list2.append(k)
print(list2)

myset1 = set(list1) #convert set into list
print(myset1)
myset2 = set(list2)
print(myset2)

if len(myset1.intersection(myset2)) > 0: #Using intersection method
    print("True..")
else:
    print("False..")
