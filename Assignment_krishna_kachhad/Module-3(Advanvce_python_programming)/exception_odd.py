# Write python program that user to enter only odd numbers, else will raise an exception.

try:
    num = int(input("Enter a number: "))
    #mod = num % 2 # Calculate the remainder when the number is divided by 2

    if num % 2==0:
        raise ValueError
    print(num)
        
except:
    print("error..")


#---------------------------------------------------------------------------------

while True:
    try:
        num = int(input("Enter a odd number: "))
        if num % 2==0: 
            raise ValueError("plz enter odd no")
        break
    except ValueError as e:
        print(e)