# Write a Python program to convert a list of tuples into a dictionary.

#----------------Using dict setdefault() method-------------

tups = [("akash", 10), ("gaurav", 12), ("anand", 14),
        ("suraj", 20), ("akhil", 25), ("ashish", 30)]
dictionary = {}
for key, val in tups:
    dictionary.setdefault(key, val)
print(dictionary)


#-------------------using append()-------------------------------

l = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
result = {}
for key, value in l:
    result.setdefault(key, []).append(value)
print (result)
