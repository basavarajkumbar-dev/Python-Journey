from tkinter import messagebox

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        messagebox.showwarning(title="Transaction Alert!", message=f"₹{amount} has credited to {self.account_number} successfully!!")
        return True
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            messagebox.showwarning(title="Transaction Alert!", message=f"₹{amount} has depited from {self.account_number} successfully!!")
            return True
        else:
            messagebox.showerror(title="Error", message=f"Please enter the valid amount, Current balance : ₹{self.balance}")
            return False
    
    def get_balance(self):
        messagebox.showinfo(title="Balance", message=f"Current Balance: ₹{self.balance}")

    def display_account_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ₹{self.balance}")

        

    
    


