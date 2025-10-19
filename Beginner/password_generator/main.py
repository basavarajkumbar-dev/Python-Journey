import string
from password_manager import *

# Lowercase letters
lowercase_letters = list(string.ascii_lowercase)
# Uppercase letters
uppercase_letters = list(string.ascii_uppercase)
#Digits
numbers = list(string.digits)
#Special Characters
charcaters = list(string.punctuation)

file_name = "passwords.txt"

container = []

print("welcome to Password Generator")

while True:
    print("1. Generate Password and Save to file\n2. Add Password and Save to file\n3. View Passwords\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        account_name = input("Enter the Account Name: ")
        password_length = int(input("Enter the Password length: "))
        if input("Do you want to add lowercase letters? (yes/no): ").lower() == "yes":
            container.append(lowercase_letters)
        if input("Do you want to add upper letters? (yes/no): ").lower() == "yes":
            container.append(uppercase_letters)
        if input("Do you want to add numbers? (yes/no): ").lower() == "yes":
            container.append(numbers)
        if input("Do you want to add special characters? (yes/no): ").lower() == "yes":
            container.append(charcaters)

        passwd = generate_password(password_length, container)
        add_password(account_name, passwd)
    elif choice == "2":
        try: 
            account_name = input("Enter the account name: ")
            password = input("Enter the Password: ")

            if not account_name or not password:
                raise ValueError("The Account name or Password should not be empty")
        except ValueError as e:
            print(f"Error: {e}")
        else:
            add_password(account_name, password)
    elif choice == "3":
        try:
            account_name = input("Enter the account name: ")
            if not account_name:
                raise ValueError("The Account name or Password should not be empty")
        except ValueError as e:
            print(f"Error: {e}")
        else:
            view_password(account_name)
    elif choice == "4":
        print("Thanks for using Password Generator!")
        print("Goodbye!")
        break
    else:
        print("Invalid input! Enter a valid input.")
    



