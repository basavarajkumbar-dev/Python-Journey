from bank_account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance):
        super().__init__(account_number, account_holder, balance)
        
        self.interest_rate = 0.08

    def add_interest(self):
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount
        print(f"Interest of {interest_amount} has been added.")