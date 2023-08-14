#Write a python program to sum of the first n positive integers.

#--------------- Using formula----------------
n = int(input("Input a number: "))
total = (n * (n + 1)) / 2
print("Sum of the first", n ,"positive integers:", total)


#--------------- Using for loop----------------
n = int(input("Input a number: "))
sum = 0
for i in range(1,n+1):
  sum = sum + i

print(sum)