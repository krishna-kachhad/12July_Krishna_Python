# Write a Python program to check multiple keys exists in a dictionary.

#------------------Using comparison operator -------------
student = {'name': 'Ram', 'age': 23, 'city': 'Rajkot'}

print(student.keys() >= {'age', 'name'})
print(student.keys() >= {'city', 'Ram'})
print(student.keys() >= {'city', 'Rajkot'})


#-----------------Using issubset() method-------------------------
sports = {"geeksforgeeks" : 1, "practice" : 2, "contribute" :3}
 
# creating set of keys that we want to compare
s1 = set(['geeksforgeeks', 'practice'])
s2 = set(['geeksforgeeks', 'ide'])
 
print(s1.issubset(sports.keys())) #z = x.issubset(y)----Return True if all items in set x are present in set y.
print(s2.issubset(sports.keys()))
