# Write a Python script to print a dictionary where the keys are numbers between 1 and 15. 
   # and the values are the square of the keys.

my_dict = dict()
for x in range(1,16):
    my_dict[x]=x**2
print(my_dict)  