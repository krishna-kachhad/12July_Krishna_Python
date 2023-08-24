import random 
def getdata():
        x = random.randint(1,100)
        nm =input("Enter name:".isupper())
        sub = input("Enter sub:")
        city = input("Enter city")

        print("Id", x)
        print("Name:",nm)
        print("Subject:",sub)
        print("city:", city)
getdata()