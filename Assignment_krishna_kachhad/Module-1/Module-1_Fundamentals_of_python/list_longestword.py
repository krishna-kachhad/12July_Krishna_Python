# Write a Python function that takes a list of words and returns the length of the longest one.

a=[]
n=int(input("Enter the number of elements in list:"))

for x in range(0,n):
    elements=input("Enter elements " + str(x+1) + ":")
    a.append(elements)

max1=len(a[0]) # Assuming that the first element in the list has the longest length,its length is stored in a variable to be compared with other lengths later in the program.
#temp=a[0] # first element is copied to a temporary variable

for i in a: #for loop is used to traverse through the elements in the list
    if(len(i)>max1): #if statement then compares the lengths of other elements with the length of the first element(max1)in the list
       max1=len(i)
       temp=i
print("The word with the longest length is:")
print(temp)