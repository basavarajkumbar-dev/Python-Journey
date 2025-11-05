from bank_account import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance):
        super().__init__(account_number, account_holder, balance)

        self.transaction_limit = 50000

    def withdraw(self, amount):
        if amount > self.transaction_limit:
            print(f"You have entered more than transaction limit, transaction limit: {self.transaction_limit}")
            return False
        else:
            super().withdraw(amount)
            return True
        