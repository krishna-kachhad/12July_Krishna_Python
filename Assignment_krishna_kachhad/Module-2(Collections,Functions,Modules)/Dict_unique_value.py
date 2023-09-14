# Write a Python program to print all unique values in a dictionary.

#-----------------------Using set + comprehension-------------------------

L = [{"abc":"movies"}, {"abc": "sports"}, {"abc": "music"}, {"xyz": "music"}, 
     {"pqr":"music"}, {"pqr":"movies"},{"pqr":"sports"}, {"pqr":"news"}]
print("Original List: ",L)

u_value = set( val for dic in L for val in dic.values())
print("Unique Values: ",u_value)

#---------------------Using extend() and sort() list methods----------------

test_dict = {'gfg' : [5, 6, 7, 8],
            'is' : [10, 11, 7, 5],
            'best' : [6, 12, 10, 8],
            'for' : [1, 2, 5]}
print("The original dictionary is : " + str(test_dict))
 
x=list(test_dict.values())
y=[]
res=[]
for i in x:
    y.extend(i)
print(y)
for i in y:
    if i not in res:
        res.append(i)
res.sort()
 
print("The unique values list is : " + str(res))