#1st pattern
'''
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''
for a in range(1,6):
    for b in range(1,6):
        print(" * ",end=" ")
    print()

#2nd pattern r=row c=column
'''
*
* *
* * *
* * * *
* * * * *
'''
for r in range(1,6):
    for c in range(r): #r means ending no
        print("*", end=" ")
    print()