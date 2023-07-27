#1 example
k=int(input("enter a "))
c=int(input("enter b "))

if k>c:
    print("a is greater")
else:
    print("b is greater")

#2 example (modulus)
num=int(input("enter no "))

if num % 2 == 0:
    print ("it is even no")
else:
    print ("it is odd no")

#3 example (short hand if else)
a = 2
b = 330

print("A") if a > b else print("B")