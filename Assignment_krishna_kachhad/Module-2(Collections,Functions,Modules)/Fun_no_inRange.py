# Write a Python function to check whether a number is in a given range.

def test_range(n):
    if n in range(10,20):
        print( "Number %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")

n = int(input("Enter no: "))
test_range(n)