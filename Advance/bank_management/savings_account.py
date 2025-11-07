from bank_account import BankAccount
from tkinter import messagebox

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance):
        super().__init__(account_number, account_holder, balance)
        
        self.interest_rate = 0.08
        self.minimum_balance = 1000

    def add_interest(self):
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount
        messagebox.showwarning(title="Interest Rate", message=f"Interest of {interest_amount} has been added.")

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            messagebox.showerror(title="Error", message=f"Can not withdraw, minimum balance of ₹{self.minimum_balance} is requaired!")
            return False
        return super().withdraw(amount)