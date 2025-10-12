print("Welcome to Password Manager!")

def add_password(account_name, password):
    with open("passwords.txt", "a") as f:
        f.write(f"{account_name}|{password}\n")
        print(f"your {account_name} password added successfully.")

def view_password(account_name):
    with open(f"passwords.txt", "r") as f:
        read_line = f.readlines()
        for line in read_line:
            a_name, passw = line.split("|")
            if a_name.lower() == account_name.lower():
                print(f"Account Name: {account_name}, Password: {passw}".rstrip())


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

