a=90
b=10
print(a,b)

#first method
c=a#90
a=b#10
b=c#90
print(a)
print(b)

#second method
a=30
b=40
a,b=b,a
print("A:",a)
print("B:",b)
