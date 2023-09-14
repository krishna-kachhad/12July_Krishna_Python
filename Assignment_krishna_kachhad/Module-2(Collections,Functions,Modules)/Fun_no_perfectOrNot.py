# Write a Python function to check whether a number is perfect or not.
'''Example : The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, 
     and 1 + 2 + 3 = 6. Equivalently, the number 6 is equal to half the sum of all its positive divisors: 
     ( 1 + 2 + 3 + 6 ) / 2 = 6. The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. 
     This is followed by the perfect numbers 496 and 8128.'''
#----------------------Using function-------------------------
def perfect(n):
    sum = 0
    
    for i in range(1,n):
        if n%i==0:
            sum += i

    return sum == n

number = int(input('Enter number: '))
# Function call & Decision
if perfect(number):
    print('%d is PERFECT' %(number))
else:
    print('%d is NOT PERFECT' %(number))

#------------------Using loop & condition-----------------------
n = int(input("Enter any number: "))
sum = 0
for i in range(1, n):
    if(n % i == 0):
        sum = sum + i
if (sum == n):
    print("The number is a Perfect number!")
else:
    print("The number is not a Perfect number!")