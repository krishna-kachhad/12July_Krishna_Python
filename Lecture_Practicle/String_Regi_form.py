fnm=input("Enter your first name:")
lnm=input("Enter your last name:")

#nested if
if fnm.isupper() and lnm.isupper():

    email=input("Enter your email:")
    mobile=input("Enter your mobile number:")

    if email.islower() and mobile.isdigit() and len(mobile) == 10:
            print("Firsname:",fnm)
            print("Lastname:",lnm)
            print("Email:",email)
            print("Mobile:",mobile)

            pwd=input("Enter password:")
            cpwd=input("Enter confirm password:")

            if pwd == cpwd:
                 print("Firsname:",fnm)
                 print("Lastname:",lnm)
                 print("Email:",email)
                 print("Mobile:",mobile)
                 print("Enter password:",pwd)
                 print("Confirm password:",cpwd)
            else:
                 print("Oops! Invalid password")   
    else:
        print("please enter valid email and mobile no")
else:
    print("Error! enter Firstname and Lastname in uppercase")


