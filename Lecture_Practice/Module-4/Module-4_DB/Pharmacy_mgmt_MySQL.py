import pymysql
import re

try:
    dbcon=pymysql.connect(host='127.0.0.1',user='root',password='',database='Pharmacy_management_system')
    print("Database connected!")
except Exception as e:
    print(e)


 # ------------------------------------ Creating the class of the system  ---------------------------------------------------

class PharmacyManagementSystem:

    ##### MEDICINE VARIABLE ######
    SR_No = 0
    Medicine_Name = ''
    Qty = ''
    Added_date = ''
    Added_by = ''
    price = ''

    ##### MANAGER VARIABLE ######
    Manager_Name = ''
    Pharmacy_Name = ''

    ##### signup & login VARIABLE ######
    username = ''
    passwd = ''
    re_passwd = ''
    email = ''
    contactno = ''

# ------------------------------------ ------------Function to call main display ---------------------------------------------------
    display = ''
    def main(self):
        print("WELCOME TO PHARMACY MANAGEMENT SYSTEM".center(70))
        print("\t 1. Admin")
        print("\t 2. Pharmacy Manager")
        print("\t 3. Exit")
        
        self.display = input("Enter your Choice: ")
        if self.display == '1':
            self.Admin()
        elif self.display == '2':
            self.pharmacy_manager()
        elif self.display == '3':
            print("Thankyou!")
        else:
            exit()
            
        
# ------------------------------------ ------------Menu function for pharmacy manager ---------------------------------------------------
    select = ''
    n = ''
    def pharmacy_manager(self):
        print("*****-----Pharmacy Manager-----*****")
        print("\t 1.Can Register")
        print("\t 2.Can Login")
        print("\t 3.Can Add Medicine")
        print("\t 4.Can View Medicine")
        print("\t 5.Can Delete Medicine")
        print("\t 6.Exit")
        self.n= input("Enter your Choice: ")
        while True:
            if self.n == '1':
                self.signup()
            elif self.n == '2':
                self.login()
            elif self.n == '3':
                self.med_add()
            elif self.n == '4':
                self.med_view()
            elif self.n == '5':
                self.med_del()
            elif self.n == '6':
                print("Exit")
            else:
                print("please enter valid input...")
            
            self.select = input("Do you want to perform more operations : press y for yes and n for no : ")
            if self.select == 'y':
                self.pharmacy_manager()
            else:
                print("Thankyou!.....")
                exit()
            
    
# ------------------------------------ ------------Menu function for pharmacy manager ---------------------------------------------------
    def Admin(self):
        print("*****-----Admin-----*****")
        print("\t 1.Can Register")
        print("\t 2.Can Login")
        print("\t 3.Can View Manager")
        print("\t 4.Can View Medicine")
        print("\t 5.Exit")
        self.n= input("Enter your Choice: ")
        while True:
            if self.n == '1':
                self.signup()
            elif self.n == '2':
                self.login()
            elif self.n == '3':
                self.manager_view()
            elif self.n == '4':
                self.Admin_med_view()
            elif self.n == '5':
                print("Exit")
            else:
                print("please enter valid input...")
            
            self.select = input("Do you want to perform more operations : press y for yes and n for no : ")
            if self.select == 'y':
                self.Admin()
            else:
                print("Thankyou!.....")
                exit()
        

# --------------------------------------------- Function for registration a new user ---------------------------------------------------

    def signup(self):
        self.username= input("Enter your Username: ")
        self.passwd = input("Enter your password: ")
        self.re_passwd = input("Enter Re-password: ")
        self.email = input("Enter your Email ID: ")
        self.contactno = input("Enter your contact No.: ")

        email_pattern="^[a-z0-9_]+[@]+[a-z]+[\.]+[a-z]"
        x=re.findall(email_pattern, self.email)

        '''signup_view = f"select * from Signup where E_mail = {self.email}"
        cr=dbcon.cursor()
        cr.execute(signup_view)

        s = cr.fetchone()
        print(s)
        if s:
            print("Account already exist! ")'''
        
        if self.username == "" or self.passwd == "" or self.re_passwd == "" or self.email == "" or self.contactno == "":
            print("Please fill out all field")
        elif self.passwd != self.re_passwd:
            print("Oops!... Incorrect password")
        elif not x:
            print("Invalid Email Address ! ")
        else:
            signup_tbl="create table if not exists Signup(U_id integer primary key auto_increment, Username varchar(40), Password varchar(40), Re_password varchar(40), E_mail text, Contact_no varchar(20))"
            signup = f"insert into Signup(Username, Password, Re_password, E_mail, Contact_no)values('{self.username}','{self.passwd}','{self.re_passwd}','{self.email}','{self.contactno}')"
            try:
                cr=dbcon.cursor()
                cr.execute(signup_tbl)
                cr.execute(signup)
                dbcon.commit()
                print("Signed Up Successful...")
            except Exception as e:
                print(e)

# --------------------------------------------- Function for login user ---------------------------------------------------

    def login(self):
        self.username= input("Enter your Username: ")
        self.passwd = input("Enter your password: ")
        
        login_tbl="create table if not exists Login(U_id integer primary key auto_increment, Username varchar(40), Password varchar(40))"
        login = f"insert into Login(Username, Password)values('{self.username}','{self.passwd}')"

        if self.username == "" or self.passwd == "":
            print("Invalid! Please Provide username and password")
        else:
            #login = f"insert into Login(Username, Password)values('{self.username}','{self.passwd}')"
            try:
                cr=dbcon.cursor()
                cr.execute(login_tbl)
                cr.execute(login)
                dbcon.commit()
                print("Login Successful...")
            except Exception as e:
                print(e)
        
        

# ------------------------------------ Function to add medicine in medicine table---------------------------------------------------
    def med_add(self):
        self.Medicine_Name = input("Enter Medicine Name: ")
        self.Qty = input("Enter Quantity: ")

        self.Added_date = input("Enter Date in YYYY-MM-DD format: ")
        pattern = r"\d{4}-\d{2}-\d{2}"
        self.date1 = re.match(pattern, self.Added_date)

        self.Added_by = input("Enter Added_by: ")
        self.price = input("Enter Price of Medicine: ")

        Add_med=f"insert into Medicine(Medicine_Name, Qty, Added_date, Added_by, price)values('{self.Medicine_Name}','{self.Qty}','{self.Added_date}','{self.Added_by}','{self.price}')"
        try:
            cr=dbcon.cursor()
            cr.execute(Add_med)
            dbcon.commit()
            print("Medicine Inserted!")
        except Exception as e:
            print(e)

# ------------------------------------ Function to view medicine in medicine table---------------------------------------------------
    def med_view(self):
        View_med="select * from Medicine"
        try:
            print("*****************===== Medicine Table =====*********************")
            cr=dbcon.cursor()
            cr.execute(View_med)
            data=cr.fetchall()
            #print(data)
            for i in data:
                print(i)
        except Exception as e:
            print(e)

# ------------------------------------ Function to delete medicine in medicine table---------------------------------------------------
    def med_del(self):
        print("Please! Select SR_No you want to delete medicine")
        self.SR_No = int(input("Enter SR_No: "))
        if self.SR_No > 0:
            Del_med=f"delete from Medicine where SR_No = {self.SR_No}"
            try:
                cr=dbcon.cursor()
                cr.execute(Del_med)
                dbcon.commit()
                print("Medicine deleted!")
            except Exception as e:
                print(e)
        else:
            print("zero SR_No is not valid....")

# ------------------------------------------ Function to add manager---------------------------------------------------------------------
    def manager_add(self):
        self.Manager_Name = input("Enter Manager Name: ")
        self.Pharmacy_Name = input("Enter Pharmacy Name: ")

        Add_manager=f"insert into Manager(Manager_Name, Pharmacy_Name)values('{self.Manager_Name}','{self.Pharmacy_Name}')"
        try:
            cr=dbcon.cursor()
            cr.execute(Add_manager)
            dbcon.commit()
            print("Data Added Successfully!")
        except Exception as e:
            print(e)

# ------------------------------------ Function to view manager in manager table---------------------------------------------------
    def manager_view(self):
        View_manager="select * from Manager"
        try:
            print("*****************===== Manager Table =====*********************")
            cr=dbcon.cursor()
            cr.execute(View_manager)
            data=cr.fetchall()
            #print(data)
            for i in data:
                print(i)
        except Exception as e:
            print(e)

# ------------------------------------ Function to view medicine in medicine table---------------------------------------------------
    def Admin_med_view(self):
        AdminView_med="select SR_No, Medicine_Name, Added_date, Added_by, price from Medicine"
        try:
            print("*****************===== Medicine Table =====*********************")
            cr=dbcon.cursor()
            cr.execute(AdminView_med)
            data=cr.fetchall()
            #print(data)
            for i in data:
                print(i)
        except Exception as e:
            print(e)




a = PharmacyManagementSystem()
a.main()