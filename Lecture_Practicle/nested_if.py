#1st program
'''a=10
b=20
c=30

if a>b:
   if a>c:
       print("a is greater")
   else:
       print("c is greater")
else:
   if b>c:
       print("b is greater")
   else:
       print("c is greater")'''

#2nd program(result)
s1=int(input("Enter Subject1:"))
s2=int(input("Enter Subject2:"))
s3=int(input("Enter Subject3:"))
s4=int(input("Enter Subject4:"))

if s1>=40 and s2>=40 and s3>=40 and s4>=40: #root (parent)
    total=s1+s2+s3+s4
    print("Total:",total)

    pr=total/4
    print("PR:",pr)

    if pr>=70: #child
        print("Result:Dist.")
    elif pr>=60: #child
        print("Result:First Class")
    elif pr>=50: #child
        print("Result:Second Class")
    elif pr>=40: #child
        print("Result:Pass Class")

else:
    print("Result:FAIL") 