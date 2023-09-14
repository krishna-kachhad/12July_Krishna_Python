# Write a Python program to check whether a list contains a sub list.


#-----------------------Using set() intersection--------------------
test_list = [5, 6, 3, 8, 2, 1, 7, 1]
print("The original list : " + str(test_list))
sublist = [8,2,1]
 
# Check for Sublist in List
if set(sublist).intersection(set(test_list)) == set(sublist):
    res = True
else:
    res = False
 
print("Is sublist present in list ? : " + str(res))
