from bank import Bank
from savings_account import SavingsAccount

print("Welcome to Basava National Bank🏦")

def get_valid_amount():
    try:
        amount = get_valid_amount()

        if amount < 0:
            raise ValueError("Amount should be greater than 0")
    except ValueError as e:
        print(f"Error: {e}")

bank = Bank()

while True:
    print("Menu:\n1. Create New Account\n2. Deposit\n3. Withdraw\n4. Transfer\n5. Check Balance\n6. Display All Accounts\n7. Apply Interest rate(for Savings Account)\n8. Exit")

    choice = input("Enter the choice: ")

    if choice == "1":
        try:
            name = input("Enter the name: ")
            account_type = input("Enter Account type(Savings/Checking): ")
            balance = int(input("Enter the initial balance: "))

            if not name or not account_type:
                raise ValueError("name or account type shouldn't be empty!")
        except ValueError as e:
            print(f"Error: {e}")
        else:
            bank.create_account(name=name, type=account_type, initial_balance=balance)

    elif choice == "2":
        account_number = input("Enter your account number: ")
        amount = get_valid_amount()
        account = bank.find_account(account_number=account_number)
        if account:
            account.deposit(amount)
    elif choice == "3":
        account_number = input("Enter your account number: ")
        amount = get_valid_amount()
        account = bank.find_account(account_number=account_number)
        if account:
            account.withdraw(amount)
    elif choice == "4":
        try:
            sender_account = input("Enter the sender account number: ")
            receiver_account = input("Enter the receiver account number: ")
            amount = get_valid_amount()

            if not sender_account or not receiver_account:
                raise ValueError("sender or receiver account number shouldn't be empty")
        except ValueError as e:
            print(f"Error: {e}")
        else:
            bank.transfer(from_acc=sender_account, to_acc=receiver_account, amount=amount)

    elif choice == "5":
        account_number = input("Enter your account number: ")
        account = bank.find_account(account_number=account_number)
        if account:
            account.get_balance()

    elif choice == "6":
        bank.display_all_accounts()

    elif choice == "7":
        account_number = input("Enter your account number: ")
        account = bank.find_account(account_number=account_number)
        if isinstance(account, SavingsAccount):
            account.add_interest()
        else:
            print("Interest can only be applied to Savings Accounts.")

    elif choice == "8":
        print("Thanks for Banking with us!")
        break