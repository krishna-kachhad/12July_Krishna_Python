# using format option for a
# value stored in a variable
str = "This article is written in {}"
print(str.format("Python"))
 
# formatting a string using a numeric constant
print("Hello, I am {} years old !".format(18))

#first method
id=2
name='abc'
print("my id is {}, my name is {}".format(id, name))

#second method
id=2
name='abc'
print(f"my id is {id}, my name is {name}")#using only f

#input from user
a=int(input("Enter A:"))
b=int(input("Enter B:"))
print("sum of {}".format(a+b))#first method
print(f"sum of {a} + {b} = {a+b}")#second method
