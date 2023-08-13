#Write python program that swap two number with temp variable and without temp variable.
#-----------------with temp variable--------------
a=100
b=500

temp=a
a=b
b=temp
print("value of a:", a)
print("value of b:", b)

#--------------without temp variable--------------
a=100
b=500

a,b=b,a
print("value of a:", a)
print("value of b:", b)