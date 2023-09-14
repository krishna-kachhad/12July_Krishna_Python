# Write a Python program to find the repeated items of a tuple.

var=int(input("Choice any no: "))
tup=(10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)  
a=list(tup)

for i in range(len(a)):
    count=a.count(var)
print(var,'appears',count,'times in the tuple')


#-------------------static-------------
tuplex = 2, 4, 5, 6, 2, 3, 4, 4, 7 
print(tuplex)

count = tuplex.count(4)
print(count)
