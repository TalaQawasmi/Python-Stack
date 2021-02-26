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

    def yield_interest(self):
        if self.account_balance >0:
            self.account_balance += self.account_balance*self.intRate

Tala =BankAccount(0.01,1000)
Tala.yield_interest()
Tala.display_account_info()
        
    
