class BankAccount:
    def __init__(self,int_rate,balance):
        self.intRate = int_rate
        self.account_balance = balance

    def deposit(self,amount):
        self.account_balance += amount
        return self

    def withdraw(self,amount):
        if self.account_balance <= amount:
            print("Insufficient funds : charging a $5 fee")
            self.account_balance -= 5
        self.account_balance -= amount
        return self
    
    def display_account_info(self):
        print("Balance :",self.account_balance)
        return self

    def transfer_money(self,amount):
        self.account_balance += amount
        return self
        

class User:		
    def __init__(self,name,email,int_rate,balance):
        self.name = name
        self.email = email
        self.account_balance = BankAccount(int_rate,balance)
    def make_deposit(self,amount):	
        self.account_balance.deposit(amount)
        return self

    def make_withdrawal(self,amount):
        self.account_balance.withdraw(amount)
        return self

    def display_user_balance (self):
        print("User :",self.name, "," ,"account balance:",self.account_balance.display_account_info())
        return self
    def transfer_money(self,amount):
        self.account_balance.transfer_money(amount)
        return self




Diala =User("Diala","qawasmidiala@gmail.com",0.02,1000)
Diala.make_deposit(100)
Diala.make_withdrawal(300)
Diala.display_user_balance()


    
