'''stdata={}

keys=['id','name','sub']

for i in range(len(keys)):
    v=input(f"Enter a value of {keys[i]}:")

    stdata[keys[i]]=v

print(stdata)'''

#---------------multiple times key static , value (userinput)-----------

stdata={}
keys=['id','name','sub']
n=int(input("Enter number of employee:"))

for i in range(n):

    for j in range(len(keys)):
        v=input(f"Enter a value of {keys[j]}:")

        stdata[keys[j]]=v

    print(stdata)
