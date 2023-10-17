import pymysql

try:
    dbcon=pymysql.connect(host='127.0.0.1',user='root',password='',database='Pharmacy_management_system')
    print("Database connected!")
except Exception as e:
    print(e)


 # ------------------------------------ Creating the class of the system  ---------------------------------------------------

class PharmacyManagementSystem:

# ------------------------------------ function to call the system ---------------------------------------------------
    def main(self):
        self.med_table()
        self.manager_table()
    
# ------------------------------------ Function to create medicine & manager table ---------------------------------------------------    
    def med_table(self):
        create_tbl="create table if not exists Medicine(SR_No integer primary key auto_increment, Medicine_Name text, Qty integer, Added_date date, Added_by text, price float)"
        try:
            cr=dbcon.cursor()
            cr.execute(create_tbl)
            print("Medicine Table created!")
        except Exception as e:
            print(e)

    def manager_table(self):
        create_tbl="create table if not exists Manager(SR_No integer primary key auto_increment, Manager_Name text, Pharmacy_Name text)"
        try:
            cr=dbcon.cursor()
            cr.execute(create_tbl)
            print("Manager Table created!")
        except Exception as e:
            print(e)

a = PharmacyManagementSystem()
a.main()