# Write a Python function to insert a string in the middle of a string.

#----------------Using Concatenation Operator----------------------

str1 = "Hello, "
str2 = "3.0"
inserted_str = "Python "
new_string = str1 + inserted_str + str2
print(new_string)

#---------------Using split() + slicing + join()---------------------

old_str = "Hello python"
print("The original string is : " +str(old_str))
mid_str = "3.0"

temp = old_str.split()
mid_pos = len(temp) // 2
 
new_str = temp[:mid_pos] + [mid_str] + temp[mid_pos:] #slicing

print("Final string: " , ' '.join(new_str)) #join()
