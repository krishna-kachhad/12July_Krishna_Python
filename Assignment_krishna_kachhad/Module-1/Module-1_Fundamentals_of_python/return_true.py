# Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.

x = int(input("Enter first value:"))
y = int(input("Enter second value:"))

def result(x, y): #define function
    if x == y or abs(x-y) == 5 or (x+y) == 5:
      return True
    else:
       return False
    
print(result(x, y)) #call the function