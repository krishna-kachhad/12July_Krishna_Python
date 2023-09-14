# Write a Python function to calculate the factorial of a number (a nonnegative integer).


#----------------------------Using function------------------------------

def factorial(n): 
	fact=1 
	for i in range(1,n+1): 
		fact=fact*i 
	return fact 
  
n=int(input("Enter positive number 'N': ")) 
f=factorial(n) 
print('Factorial is: ',f) 

#----------------------------Using recursion-------------------------------

def factorial(n):
    """This is a recursive function
    to find the factorial of an integer"""
    #factorial() is a recursive function that calls itself.

    if n == 1:
        return 1
    else:
        # recursive call to the function
        return (n * factorial(n-1))

num = int(input("Enter a number: "))
# call the factorial function
result = factorial(num)
print("The factorial of", num, "is", result)