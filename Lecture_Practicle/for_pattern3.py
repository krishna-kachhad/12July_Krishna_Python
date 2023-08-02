'''
1
2 2
3 3 3 
4 4 4 4 
5 5 5 5 5
'''

for r in range(1,6):
    for c in range(r):
        print(r,end=" ") #column
    print(" ") #row break

'''
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15
'''

num=1
for r in range(1,6):
    for c in range(1,r+1):
        print(num,end=" ") #column
        num=num+1
    print("") #OR print("\r") \r used for (ending line after each row)

