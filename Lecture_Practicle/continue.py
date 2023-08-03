#1st using for loop
for i in range(5):
    if i == 3:
        continue
    print(i)

#2nd program to print odd numbers from 1 to 10

num = 0

while num < 10:
    num += 1
    
    if (num % 2) == 0:
        continue
    print(num)

#3rd program to print even numbers from 1 to 10
num = 0

while num < 10:
    num += 2
    
    if (num % 2) != 0:
        continue
    print(num)