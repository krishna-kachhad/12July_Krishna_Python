# Write a python program to find the longest words.

with open('python.txt') as file:
    data=file.read().split()
    max=len(max(data,key=len ))
    print(max)
    res=[word for word in data if len(word)==max]
    print(res)