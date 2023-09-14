#global
a=34
b=56

def production():
    #local
    global a,b
    a=66
    b=89
    print("Mul:",a*b)

print("Sum:",a+b)

production()

#--------------------ppt example--------------
def myfun():
       global name
       print("1st ",name)
       name="Python Language"
       print("2nd ",name)

name="Python"

myfun()

print("3rd ",name)