# Write a Python script to sort (ascending and descending) a dictionary by value.

#------------------------using lambda function----------------------

my_dict = {'Apple':5, 'papaya':6, 'kiwi':4, 'pomegranate':11, 'strawberry':10}
print("original dictionary: ", my_dict)

asce_dict = sorted(my_dict.items(), key = lambda x:x[1])
print(asce_dict)

desc_dict = sorted(my_dict.items(), key = lambda x:x[1], reverse = True)
print(desc_dict)


#------------------------using operator-----------------------------
import operator
d = {'Apple':5, 'papaya':6, 'kiwi':4, 'pomegranate':11, 'strawberry':10}
print('Original dictionary : ',d)

sorted_d = sorted(d.items(), key=operator.itemgetter(1))
print('Dictionary in ascending order by value : ',sorted_d)

sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by value : ',sorted_d)