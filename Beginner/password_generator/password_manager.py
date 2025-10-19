from cryptography.fernet import Fernet
import random as ra

"""
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)"""

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)

def generate_password(password_length, container):
    password_lst = []

    while True:
        for var in container:
            if len(password_lst) != password_length:
                random_chr = ra.choice(var)
                password_lst.append(random_chr)
            else:
                break
        if len(password_lst) == password_length:
            break
    ra.shuffle(password_lst)
    password = "".join(password_lst)
    return password

def add_password(account_name, password):
    with open("passwords.txt", "a") as f:
        f.write(f"{account_name}|{fer.encrypt(password.encode()).decode()}\n")
        print(f"your {account_name} password added successfully.")

def view_password(account_name):
    try:
        with open("passwords.txt", "r") as f:
            for line in f:
                a_name, passw = line.split("|", 1)
                if a_name.lower() == account_name.lower():
                    try:
                        decrypted_password = fer.decrypt(passw.encode()).decode()
                        print(f"Account Name: {a_name}, Password: {decrypted_password}")
                        return 
                    except:
                        print(f"Error decrypting password for {a_name}")
                        return
            print(f"Account '{account_name}' not found!")
            
    except FileNotFoundError:
        print("Password file not found!")