class User:		
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account_balance = 0  
    def make_deposit(self,amount):	
        self.account_balance += amount
        return self

    def make_withdrawal(self,amount):
        self.account_balance -= amount
        return self

    def display_user_balance (self):
        print("User :",self.name, "," ,"account balance:",self.account_balance)
        return self
    def transfer_money(self,other_user,amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

Loay = User ("Loay","loay@gmail.com")
Tala = User("Tala Qawasmi","qawasmitala@gmail.com")
Donbok = User("Mohammad Donbok","hamoodD@gmail")
Donbok.make_deposit(400).make_withdrawal(300)
Tala.make_deposit(500).make_withdrawal(200).display_user_balance().transfer_money(Loay,100)
Loay.display_user_balance().make_deposit(300)

