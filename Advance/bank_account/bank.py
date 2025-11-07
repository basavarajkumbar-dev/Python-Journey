from bank_account import BankAccount
from savings_account import SavingsAccount
from checking_account import CheckingAccount
from tkinter import messagebox

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, type, initial_balance):
        accounts_length = len(self.accounts)
        account_number = "AC"+("0"*(8-len(str(accounts_length))))+str(accounts_length+1)

        if type == "Savings":
            new_account = SavingsAccount(account_number=account_number, account_holder=name, balance=initial_balance)
        elif type == "Checking":
            new_account = CheckingAccount(account_number=account_number, account_holder=name, balance=initial_balance)
        self.accounts[account_number] = new_account

        print("New account has been created successfully!")
        print(f"Account Details:- \nAccount number: {self.accounts[account_number].account_number}\nAccount holder: {self.accounts[account_number].account_holder}\nAccount Type: {type}\nBalance: {self.accounts[account_number].balance}")

        messagebox.showinfo(title="Account Details", 
                            message=f"New Account Created Successfuly\nAccount number: {self.accounts[account_number].account_number}\nAccount holder: {self.accounts[account_number].account_holder}\nAccount Type: {type}\nBalance: {self.accounts[account_number].balance}")

    def find_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            messagebox.showerror(title="Error", message=f"'{account_number}'Account not found")
            return False

    def display_all_accounts(self):
        all_counts = []
        if len(self.accounts) > 0:
            for numbers, account in self.accounts.items():
                all_counts.append({"account_number":account.account_number, "name": account.account_holder, "balance": account.balance})
            return all_counts
        else:
            messagebox.showerror(title="Error", message="No Accounts found!!")

    def transfer(self, from_acc, to_acc, amount):
        try:
            sender = self.find_account(account_number=from_acc)
            reciever = self.find_account(account_number=to_acc)
        except KeyError as e:
            messagebox.showerror(title="Error", message=f"Error: {e}")
        else:
            if sender and reciever:
                if sender.balance >= amount:
                    sender.balance -= amount
                    reciever.balance += amount
                    messagebox.showwarning(title="Transaction Alert!", message=f"Transfered successfully!!\n₹{amount} has been transferred from {from_acc} to {to_acc}")
                else:
                    messagebox.showerror(title="Error", message=f"Insufficient funds")
        