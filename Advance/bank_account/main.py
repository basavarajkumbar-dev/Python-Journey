import tkinter as tk
from tkinter import messagebox
from bank import Bank
from savings_account import SavingsAccount
from tkinter import ttk

bank = Bank()

def clear_right_panel():
    for widget in root.grid_slaves():
        if int(widget.grid_info()["column"]) == 1:
            widget.destroy()

def new_account():
    clear_right_panel()

    account_label = tk.Label(root, text="New Account", font=("Arial", 20, "bold"), anchor="w")
    account_label.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    name_label = tk.Label(root, text="Name:", font=("Arial", 20), anchor="w")
    name_label.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    name_entry = tk.Entry(root, width=25, font=("Arial", 20))
    name_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    type_label = tk.Label(root, text="Account Type(Savings/Checking):", font=("Arial", 20))
    type_label.grid(row=3, column=1, padx=5, pady=5,sticky="w")

    type_entry = tk.Entry(root, width=25, font=("Arial", 20))
    type_entry.grid(row=4, column=1, padx=5, pady=5,sticky="w")

    balance_label = tk.Label(root, text="Initial Balance: ", font=("Arial", 20))
    balance_label.grid(row=5, column=1, padx=5, pady=5,sticky="w")
    
    balance_entry = tk.Entry(root, width=25, font=("Arial", 20))
    balance_entry.grid(row=6, column=1, padx=5, pady=5,sticky="w")

    def submit():  
        try:
            name = name_entry.get()
            account_type = type_entry.get().strip().title()
            balance = int(balance_entry.get())

            if account_type not in ["Savings", "Checking"]:
                raise ValueError("Please enter Account Type Savings or Checking only!")

            if balance < 0:
                raise ValueError("Initial blance should be greater than 0")
            if not balance.strip():
                raise ValueError("Initial balance not entered! Please enter a valid number.")
            
            if not name or not account_type:
                raise ValueError("name or account type shouldn't be empty!")
        except ValueError as e:
            messagebox.showerror(title="Error", message=f"{e}")
        else:
            bank.create_account(name=name, type=account_type, initial_balance=balance)
        finally:
            name_entry.delete(0, tk.END)
            type_entry.delete(0, tk.END)
            balance_entry.delete(0, tk.END)

    tk.Button(root, text="Submit", font=("Arial", 20), width=20, command=submit).grid(row=7, column=1, padx=5, pady=5, sticky="w")

def deposit_amount():
    clear_right_panel()
    deposit_label = tk.Label(root, text="Deposit", font=("Arial", 20, "bold"), anchor="w")
    deposit_label.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    account_num_label = tk.Label(root, text="Account Number: ", font=("Arial", 20), anchor="w")
    account_num_label.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    account_num_entry = tk.Entry(root, width=25, font=("Arial", 20))
    account_num_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    amount_label = tk.Label(root, text="Amount: ", font=("Arial", 20))
    amount_label.grid(row=3, column=1, padx=5, pady=5,sticky="w")

    amount_entry = tk.Entry(root, width=25, font=("Arial", 20))
    amount_entry.grid(row=4, column=1, padx=5, pady=5,sticky="w")

    def submit():  
        try:
            account_number = account_num_entry.get()
            amount = int(amount_entry.get())

            if amount < 0:
                raise ValueError("Amount should be greater than 0")
            
            if not amount.strip():
                raise ValueError("Amount not entered! Please enter a valid number.")
            
        except ValueError as e:
            messagebox.showerror(title="Error", message=f"{e}")
        else:
            account = bank.find_account(account_number=account_number)
            if account:
                account.deposit(amount)
        finally:
            account_num_entry.delete(0, tk.END)
            amount_entry.delete(0, tk.END)
    
    tk.Button(root, text="Submit", font=("Arial", 20), width=20, command=submit).grid(row=5, column=1, padx=5, pady=5, sticky="w")

def withdraw_amount():
    clear_right_panel()
    deposit_label = tk.Label(root, text="Withdraw", font=("Arial", 20, "bold"), anchor="w")
    deposit_label.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    account_num_label = tk.Label(root, text="Account Number: ", font=("Arial", 20), anchor="w")
    account_num_label.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    account_num_entry = tk.Entry(root, width=25, font=("Arial", 20))
    account_num_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    amount_label = tk.Label(root, text="Amount: ", font=("Arial", 20))
    amount_label.grid(row=3, column=1, padx=5, pady=5,sticky="w")

    amount_entry = tk.Entry(root, width=25, font=("Arial", 20))
    amount_entry.grid(row=4, column=1, padx=5, pady=5,sticky="w")

    def submit():  
        try:
            account_number = account_num_entry.get()
            amount = int(amount_entry.get())

            if amount <= 0:
                raise ValueError("Amount should be greater than 0")
            if not amount.strip():
                raise ValueError("Amount not entered! Please enter a valid number.")
            
        except ValueError as e:
            messagebox.showerror(title="Error", message=f"{e}")
        else:
            account = bank.find_account(account_number=account_number)
            if account:
                account.withdraw(amount)
        finally:
            account_num_entry.delete(0, tk.END)
            amount_entry.delete(0, tk.END)

    tk.Button(root, text="Submit", font=("Arial", 20), width=20, command=submit).grid(row=5, column=1, padx=5, pady=5, sticky="w")

def balance_check():
    clear_right_panel()
    deposit_label = tk.Label(root, text="Check Balance", font=("Arial", 20, "bold"), anchor="w")
    deposit_label.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    account_num_label = tk.Label(root, text="Account Number: ", font=("Arial", 20), anchor="w")
    account_num_label.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    account_num_entry = tk.Entry(root, width=25, font=("Arial", 20))
    account_num_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
    def submit():  
        try:
            account_number = account_num_entry.get()
            
        except ValueError as e:
            messagebox.showerror(title="Error", message=f"{e}")
        else:
            account = bank.find_account(account_number=account_number)
            if account:
                account.get_balance()
        finally:
            account_num_entry.delete(0, tk.END)

    tk.Button(root, text="Submit", font=("Arial", 20), width=20, command=submit).grid(row=3, column=1, padx=5, pady=5, sticky="w")

def transfer_amount():
    clear_right_panel()

    account_label = tk.Label(root, text="Transfer", font=("Arial", 20, "bold"), anchor="w")
    account_label.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    from_label = tk.Label(root, text="Sender Account Number:", font=("Arial", 20), anchor="w")
    from_label.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    from_entry = tk.Entry(root, width=25, font=("Arial", 20))
    from_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    to_label = tk.Label(root, text="Receiver Account Number:", font=("Arial", 20))
    to_label.grid(row=3, column=1, padx=5, pady=5,sticky="w")

    to_entry = tk.Entry(root, width=25, font=("Arial", 20))
    to_entry.grid(row=4, column=1, padx=5, pady=5,sticky="w")

    amount_label = tk.Label(root, text="Amount: ", font=("Arial", 20))
    amount_label.grid(row=5, column=1, padx=5, pady=5,sticky="w")
    
    amount_entry = tk.Entry(root, width=25, font=("Arial", 20))
    amount_entry.grid(row=6, column=1, padx=5, pady=5,sticky="w")

    def submit():  
        try:
            sender_account = from_entry.get()
            receiver_account = to_entry.get()
            amount = int(amount_entry.get())

            if amount <= 0:
                raise ValueError("Amount should be greater than 0")
            
            if not amount.strip():
                raise ValueError("Amount not entered! Please enter a valid number.")

            if not sender_account or not receiver_account:
                raise ValueError("name or account type shouldn't be empty!")
        except ValueError as e:
            messagebox.showerror(title="Error", message=f"{e}")
        else:
            bank.transfer(from_acc=sender_account, to_acc=receiver_account, amount=amount)
        finally:
            from_entry.delete(0, tk.END)
            to_entry.delete(0, tk.END)
            amount_entry.delete(0, tk.END)

    tk.Button(root, text="Submit", font=("Arial", 20), width=20, command=submit).grid(row=7, column=1, padx=5, pady=5, sticky="w")

def apply_interest():
    clear_right_panel()
    header_label = tk.Label(root, text="Apply Interest rate(Savings Account)", font=("Arial", 20, "bold"), anchor="w")
    header_label.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    account_num_label = tk.Label(root, text="Account Number: ", font=("Arial", 20), anchor="w")
    account_num_label.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    account_num_entry = tk.Entry(root, width=25, font=("Arial", 20))
    account_num_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
    def submit():  
        try:
            account_number = account_num_entry.get()
        except ValueError as e:
            messagebox.showerror(title="Error", message=f"{e}")
        else:
            account = bank.find_account(account_number=account_number)
            if isinstance(account, SavingsAccount):
                account.add_interest()
            else:
                messagebox.showerror(title="Error", message="Interest can only be applied to Savings Accounts.")
        finally:
            account_num_entry.delete(0, tk.END)

    tk.Button(root, text="Submit", font=("Arial", 20), width=20, command=submit).grid(row=3, column=1, padx=5, pady=5, sticky="w")

def display_accounts():
    clear_right_panel()
    header_label = tk.Label(root, text="Accounts Details", font=("Arial", 20, "bold"), anchor="w")
    header_label.grid(row=0, column=1, columnspan=3, padx=5, pady=5)

    columns = ("Account Number", "Account Holder", "Balance")
    table = ttk.Treeview(root, columns=columns, show="headings")

    # Define headings
    for col in columns:
        table.heading(col, text=col)
        table.column(col, width=150, anchor="center")

    table.grid(row=1, column=1, columnspan=3,rowspan=8, padx=10, pady=5)
    
    accounts = bank.display_all_accounts()

    if accounts:
        for account in accounts:
           table.insert("", "end", values=(account['account_number'], account['name'], account['balance']))

# Create the main window
root = tk.Tk()
root.title("Basava International Bank")
root.geometry("820x400")

tk.Label(root, text="Menu", font=("Arial", 20, "bold")).grid(row=0, column=0, padx=5, pady=5)

tk.Button(root, text="Create New Account", font=("Arial", 20), width=25, command=new_account).grid(row=1, column=0, padx=5, pady=5)

tk.Button(root, text="Deposit", font=("Arial", 20), width=25, command=deposit_amount).grid(row=2, column=0, padx=5, pady=5)

tk.Button(root, text="Withdraw", font=("Arial", 20), width=25, command=withdraw_amount).grid(row=3, column=0, padx=5, pady=5)

tk.Button(root, text="Check Balance", font=("Arial", 20), width=25, command=balance_check).grid(row=4, column=0, padx=5, pady=5)

tk.Button(root, text="Transfer", font=("Arial", 20), width=25, command=transfer_amount).grid(row=5, column=0, padx=5, pady=5)

tk.Button(root, text="Apply Interest rate(Savings Ac)", font=("Arial", 20), width=25, command=apply_interest).grid(row=6, column=0, padx=5, pady=5)

tk.Button(root, text="Display All Accounts", font=("Arial", 20), width=25, command=display_accounts).grid(row=7, column=0, padx=5, pady=5)

# Run the application
root.mainloop()