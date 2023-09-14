#  Dictionary is a collection which is ordered, changeable and indexed. No duplicate members....

stdata={'id':1,'name':'krishna','sub':'python'}

print(stdata)
print(stdata['name']) #in dict get the value by key
#or
print(stdata.get('name'))
print(len(stdata))

print(stdata.keys())
print(stdata.values())
#====================================


for i in stdata: #return key
    print(i)

for i in stdata.values(): #return value
    print(i)

for i in stdata.items(): #returns key and value(pair)
    print(i)

#----------------------------------------
stdata['id']=2
stdata['city']='Rajkot'
stdata.pop('sub')

#stdata.clear()
print(stdata)

del stdata['name']
print(stdata)

newdict=stdata.copy()
print(newdict)