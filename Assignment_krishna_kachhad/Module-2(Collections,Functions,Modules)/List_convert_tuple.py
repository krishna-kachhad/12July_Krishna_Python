# Write a Python program to convert a list to a tuple.

#-------------------user input-----------------
list = []
n = int(input("Enter the no of elements: "))
for i in range(n):
    x = input("Enter elements: ")
    list.append(x)
tuplex = tuple(list)
print(tuplex)


#-----------------Using function with return keyword----------------
def convert_list_to_tuple(lst):
    tuple_result = ()  # Empty tuple to store the converted elements
    for element in lst:
        tuple_result += (element,)  # Append each element to the tuple
    return tuple_result
 
# Example usage
my_list = [1, 2, 3, 4]
my_tuple = convert_list_to_tuple(my_list)
print(my_tuple) 