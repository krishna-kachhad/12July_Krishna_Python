import random
r = random.randrange(111111,999999)
class Bankaccount:
    def ACopen(self):
        self.name = (input("Enter name: "))
        print("account no " , r)
        self.balance = 2500
          
    def deposit(self):
        amount = float(input("Enter amount to be deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)

    def withdraw(self):
        amount = float(input("Enter amount to be withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
            print(self.balance)
        else:
            print("\n Insufficient balance  ")
    
    def statement(self):
        print("Account name", self.name)
        print("Acc no", r)
        print("total balance", self.balance)

a = Bankaccount()
a.ACopen()
a.deposit()
a.withdraw()
a.statement()
