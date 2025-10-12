print("Welcome to Password Manager!")

def add_password(account_name, password):
    pass

def view_password(account_name):
    pass

while True:
    choice = input("Do you want add the Password or view existing one?(Type add or view or Type q for Quit): ")
    if choice == "add":
        try: 
            account_name = input("Enter the account name: ")
            password = input("Enter the Password: ")

            if not account_name or not password:
                raise ValueError("The Account name or Password should not be empty")
        except ValueError as e:
            print(f"Error: {e}")
        else:
            add_password(account_name, password)
    elif choice == "view":
        try:
            account_name = input("Enter the account name: ")
            if not account_name:
                raise ValueError("The Account name or Password should not be empty")
        except ValueError as e:
            print(f"Error: {e}")
        else:
            view_password(account_name)
    elif choice.lower() == "q":
        break
        print("Thanks for using Password Manager!")
        print("Goodbye!")

