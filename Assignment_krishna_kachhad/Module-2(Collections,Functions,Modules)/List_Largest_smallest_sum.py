# Write a Python function to get the largest number, smallest num and sum of all from a list.

list = []

n = int(input("How many numbers:" ))
for i in range(n):
    number = int(input("Enter number:" ))
    list.append(number)
    print(list)
    
print("Maximum no in the list:" , max(list))
print("Minimum no in the list:" , min(list))
print("Sum of all numbers:", sum(list))

