from bank_account import BankAccount
from savings_account import SavingsAccount
from checking_account import CheckingAccount

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
        print(f"Account Details:- \nAccount number: {self.accounts[account_number].account_number}\nAccount holder: {self.accounts[account_number].account_holder}")


    def find_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            print("Account not found")

    def display_all_accounts(self):
        if len(self.accounts) > 0:
            print(f"{'Account No':<15}{'Name':<20}{'Balance'}")
            for numbers, account in self.accounts.items():
                print(f"{account.account_number:<15}{account.account_holder:<20}{account.balance}")
        else:
            print("No Accounts found!!")

    def transfer(self, from_acc, to_acc, amount):
        try:
            sender = self.find_account(account_number=from_acc)
            reciever = self.find_account(account_number=to_acc)
    
            if not sender:
                raise KeyError(f"{from_acc} account number not found")
            
            if not reciever:
                raise KeyError(f"{to_acc} account number not found")
        except KeyError as e:
            print(f"Error: {e}")

        else:
            if sender.balance >= amount:
                if sender.withdraw(amount):
                    reciever.deposit(amount)
                    print("Transfered successfully!!")
            else:
                print("Insufficient funds")
        