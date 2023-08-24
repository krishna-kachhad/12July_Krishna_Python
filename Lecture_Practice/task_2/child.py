import random
def mydata():
    x=random.randint(1,100)
    nm=input("Enter Name: ")
    sub=input("Enter Subject: ")
    city=input("Enter City: ")

    print("Name: ", nm)
    nm1=nm.upper() #name must be capital... so using upper method
    print("Subject: ", sub)
    print("city: ", city)
    list=[x,nm1,sub,city]
    print(list)

def mydata2():
    list=[]
    for i in range(5):
        x=random.randint(1,100)
        nm=input("Enter Name: ")
        sub=input("Enter Subject: ")
        city=input("Enter City: ")

        print("Name: ", nm)
        nm1=nm.upper()          #name must be capital... so using upper method
        print("Subject: ", sub)
        print("city: ", city)
        li = (x,nm1,sub,city)
        print(li)
        list.append(li)
    print(list)








