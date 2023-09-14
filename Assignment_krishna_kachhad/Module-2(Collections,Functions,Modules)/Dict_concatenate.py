# Write a Python script to concatenate following dictionaries to create a new one.

#-----------------using update() method----------------
my_dict_1 = {'J':12,'W':22}
my_dict_2 = {'M':67}

my_dict_1.update(my_dict_2)
print("The concatenated dictionary is :")
print(my_dict_1)

#---------------------------------------------------------
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): 
    dic4.update(d)
print(dic4)

#-------------------using unpack operator (**)-------------
dict_1 = {'A': 15, 'B': 10, 'C' : 12 }  
dict_2 = {'E': 18,'B': 20,'D' : 16 }  
d3 = {**dict_1,**dict_2}  
print(d3)  