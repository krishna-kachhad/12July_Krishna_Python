# Set is a collection which is unordered and unindexed. No duplicate members.

myset={'A','B','C','D','E','F'}
print(myset)

print(len(myset))

if 'B' in myset:
    print("Yes...")
else:
    print("Noo")

for i in myset:
    print(i)
#--------------------------------
print(myset)
myset.add('G') #for add single element
myset.update(['H','I','J','A','B']) #for multiple elements ans written in []
print(myset)
myset.remove('C')
print(myset)
myset.clear()
#---------------------------------------
print(myset)
myset.remove('b')#its give error coz lowerclass
myset.discard('b')# its not give error ....output return as it is

newset={'P','Q','R','S','A','C'}
print(newset)

#x=myset.union(newset)
x=myset.intersection(newset)
print(x)



