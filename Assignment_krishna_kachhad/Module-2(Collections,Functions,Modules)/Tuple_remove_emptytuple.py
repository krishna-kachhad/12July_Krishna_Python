# Write a Python program to remove an empty tuple(s) from a list of tuples.

L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
L = [t for t in L if t]
print(L)




#-----------------using filter() method-----------------

list_1 =  [(), ('okay','10','11'), (), ('lock', 'key'),  
          ('kite', '12'),()] 
filter_items = filter(lambda x: x != (), list_1)
remove_tuples = list(filter_items)
print(remove_tuples)