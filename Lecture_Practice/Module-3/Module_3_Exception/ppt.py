# exception demo 

a= int(input("Enter the value of A :"))
b= int(input("Enter the value of B :"))

try:
    c=a/b 
    print("Division : ",c)
except Exception:
    print("Execption Caught")
    
    
print("Bye")


# exception demo 

from builtins import int
while True:
    try:
        n=input("Enter the value : ")
        n=int(n)
        break
    except Exception:
        print("Invalid Input")
    finally:
        print("Finally Called")
print("Bye")