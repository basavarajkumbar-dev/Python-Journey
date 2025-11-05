class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} has credited to {self.account_number} successfully!!")
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} has depited from {self.account_number} successfully!!")
        else:
            print(f"Please enter the valid amount, Current balance : ₹{self.balance}")
    
    def get_balance(self):
        print(f"Current Balance: ₹{self.balance}")

    def display_account_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ₹{self.balance}")

        

    
    


