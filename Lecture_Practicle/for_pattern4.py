'''
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
'''

for r in range(5,0,-1):
    for c in range(r):
        print(r,end=" ") #column
    print(" ") #row break

'''
5 5 5 5 5
3 3 3
1
'''

for r in range(5,0,-2):
    for c in range(r):
        print(r,end=" ") #column
    print(" ") #row break