fruit=['apple', 'banana', 'grapes', 'orange', 'mango']

print(fruit)
print(fruit[0])
print(fruit[-2])
print(fruit[2:])
print(fruit[:4])
print(fruit[1:3])
print(fruit[-4:-1])
print(fruit)
#change the 2nd value by replacing it with two new values
fruit[1:2] = 'melon', 'blackcurrent' 
print(fruit)

fruit1=['apple','banana', 56, True, 'abc', 9] #a list can contain different data tyeps...string,int,float,boolean
print(fruit1)

fruit=['apple', 'banana', 'grapes', 'orange', 'mango']
print(len(fruit))
print(type(fruit))
fruit[2]='kiwi'
print(fruit)

if 'apple' in fruit:
    print("yes, in list")


#---------------------list method-----------------
fruit=['apple', 'banana', 'grapes', 'orange', 'mango']
print(fruit.append('cherry')) #add item at last 
print(fruit)
fruit.insert(3,'melon')
print(fruit)
fruit.reverse()
print(fruit)
fruit.sort() #sort ascending order alphabetically
print(fruit) 
fruit.sort(reverse=True) #sort descending order
print(fruit)
fruit.pop() #remove last item
print(fruit)
fruit.pop(0) #remove 0 index item
print(fruit)
fruit.remove('melon') #remove specified item
print(fruit)
fruit.clear() #clear the list
print(fruit) 

fruit=['apple', 'banana', 'grapes', 'orange', 'mango']
del fruit[1] #del KEYWORD removes specified index
print(fruit)
del fruit #delete completely

#--------------------copy list---------------------
list1=['apple','banana']
mylist=list1.copy() #copy of a list
print(mylist)

#---------------------join two lists-------------------
#using +
list1=[1,2,3]
list2=['kiwi', 'orange', 'mango']
list3=list1+list2
print(list3)
#using append() method
list1=[1,2,3]
list2=['kiwi', 'orange', 'mango']
for x in list2:
    list1.append(x)
print(list1)
#using extend() method
list1=[1,2,3]
list2=['kiwi', 'orange', 'mango']
list1.extend(list2)
print(list1)
