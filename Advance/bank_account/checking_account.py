from bank_account import BankAccount
from tkinter import messagebox

class CheckingAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance):
        super().__init__(account_number, account_holder, balance)

        self.transaction_limit = 50000

    def withdraw(self, amount):
        if amount > self.transaction_limit:
            messagebox.showwarning(title="Transaction Alert!", message=f"Transaction limit excceeded. Limit: {self.transaction_limit}")
            return False
        elif amount > self.balance:
            messagebox.showwarning(title="Transaction Alert!", message=f"Insufficient funds. Current Balance: {self.balance}")
        else:
            super().withdraw(amount)
            return True
        