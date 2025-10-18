import csv
from tabulate import tabulate
from datetime import datetime

print("Welcome to Personal Finance Tracker!")

filename = "transactions.csv"

def load_from_file(filename):
    with open(filename, "r", newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        transactions_list = []
        for item in reader:
            transcation = {
                'id': item["ID"],
                'date':item["DATE"],
                'type':item["TYPE"],
                'amount': item["AMOUNT"],
                'category': item["CATEGORY"],
                'description': item["DESCRIPTION"]
            }
            transactions_list.append(transcation)
    
    return transactions_list

transactions_list = load_from_file(filename)

def add_transaction(transactions_list, transaction_type):
    print(f"=== ADD {transaction_type.upper()} ===")
    def is_valid_date(date):
            try:
                # Try to parse the string into a datetime object      
                entered_date = datetime.strptime(date, "%Y-%m-%d").date()
                today = datetime.today().date()
                return entered_date <= today

            except ValueError:
                # If parsing fails, it's not a valid date in the correct format
                return False
            
    try:
        date = input("Enter the date(YYYY-MM-DD): ")
        if not is_valid_date(date):
            raise ValueError("Enter the valid date!")
        
        amount = input("Enter the amount: ")
        if not amount.isdigit():
            raise ValueError("Please enter a valid number(ex: 150 or 100).")

        category = input("Enter category: ")
        description = input("Enter description: ")
        
        if not date or not amount or not category or not description:
            raise ValueError("Please enter all the sections!")

    except ValueError as e:
        print(f"Error: {e}")

    else:
        transaction = {
            "id": len(transactions_list) + 1,
            "date": date,
            "type": transaction_type,
            "amount": amount,
            "category": category,
            "description":description
        }
        transactions_list.append(transaction)

        print(f"{transaction_type} added successfully!")


def calculate_balance(transactions_list):
    if len(transactions_list) <= 0:
        print("You don't have any transaction history, Please add income or expenses!")
    else:
        print("=== CURRENT FINANCIAL SUMMARY ===")
        total_income = 0
        total_expense= 0
        for transaction in transactions_list:
            if transaction["type"].lower() == "income":
                total_income += int(transaction["amount"])
            elif transaction["type"].lower() == "expense":
                total_expense += int(transaction["amount"])
        
        total_balance = total_income - total_expense
        print(f"Total Income: ₹{total_income}\nTotal Expense: ₹{total_expense}")
        print("-------------------------------")
        print(f"Current Balance: ₹{total_balance}")
            

def view_transactions(transactions_list):
    print("=== ALL TRANSACTIONS ===")
    if len(transactions_list) > 0:
        table = tabulate(transactions_list, headers="keys", tablefmt="grid")
        print(table)
        print("Total transactions: ", len(transactions_list))


def save_to_file(transactions_list, filename):
    with open(filename, "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["ID", "DATE", "TYPE", "AMOUNT", "CATEGORY", "DESCRIPTION"])
        writer.writeheader()
        for transaction in transactions_list:
            writer.writerow({"ID": transaction["id"], 
                             "DATE": transaction["date"], 
                             "TYPE":transaction["type"], 
                             "AMOUNT": transaction["amount"],
                             "CATEGORY": transaction["category"],
                             "DESCRIPTION": transaction["description"]})
    print("Your data saved successfully")


def spending_by_category(transactions_list):
    total_expense = sum(int(transaction["amount"]) for transaction in transactions_list if transaction["type"] == "Expense")
    category_total = {}
    for transaction in transactions_list:
        if transaction["type"] == "Expense":
            category = transaction["category"]
            amount = int(transaction["amount"])
            category_total[category] = category_total.get(category, 0) + amount

    print("\n=== SPENDING BY CATEGORY ===")
    print(f"{'Category':<15} {'Amount':<10} {'Percentage'}")
    print("-" * 40)
    
    for category, total in category_total.items():
        percentage = (total / total_expense) * 100
        print(f"{category:<15} ₹{total:<9.2f} {percentage:.1f}%")
    
    print(f"\nTotal Expenses: ₹{total_expense:.2f}")

def monthly_summary(transactions_list):
    if not transactions_list:
        print("You don't have any transactions history!")

    monthly_data = {}
    for transaction in transactions_list:
        date = transaction["date"]
        month = date[:7]
        amount = int(transaction["amount"])
        transact_type = transaction["type"]

        if month not in monthly_data:
            monthly_data[month] = {"income": 0, "expense": 0}

        if transact_type.lower() == "income":
            monthly_data[month]["income"] += amount
        else:
            monthly_data[month]["expense"] += amount
        
    for month, data in monthly_data.items():
        income = data["income"]
        expense = data["expense"]
        savings = income - expense

        if savings > 0:
            savings_percentage = (savings/income) * 100
        else:
            savings_percentage = 0

        monthly_data[month]["savings"] = savings
        monthly_data[month]["savings_percentage"] = savings_percentage

    sorted_months = sorted(monthly_data.keys())

    print("\n=== MONTHLY SUMMARY ===")
    print(f"{'Month':<10} {'Income':<10} {'Expenses':<10} {'Savings':<10} {'Savings %'}")
    print("-" * 55)

    for month in sorted_months:
        data = monthly_data[month]
        print(f"{month:<10} ₹{data['income']:<9.2f} ₹{data['expense']:<9.2f} "
              f"₹{data['savings']:<9.2f} {data['savings_percentage']:.1f}%")
    
    # Find best savings month
    if monthly_data:
        best_month = max(monthly_data.keys(), 
                        key=lambda m: monthly_data[m]['savings_percentage'])
        best_percentage = monthly_data[best_month]['savings_percentage']
        print(f"\n★ Best savings month: {best_month} ({best_percentage:.1f}%)")

def search_transactions(transactions_list, category):
    search_category = []
    for transact in transactions_list:
        if transact['category'] == category:
            search_category.append({"date": transact["date"], "amount": int(transact["amount"]), "type":transact["type"], "description":transact["description"]})

    if search_category:
        print("\n=== Search Results BY CATEGORY ===")
        print(f"{'Date':<12}{'Type':<10}{'Amount':<12}{'Description'}")
        print("-" * 40)
        for item in search_category:
            print(f"{item['date']:<12}{item['type']:<10}₹{item['amount']:<9.2f}{item['description']}")

while True:
    print("1. View All Transactions\n2. Add Income\n3. Add Expense\n4. Show Current Balance\n5. Spending by Category\n6. Monthly Summary\n7. Search by Category\n8. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        view_transactions(transactions_list=transactions_list)
    elif choice == "2":
        transaction_type = "Income"
        add_transaction(transactions_list, transaction_type)
    elif choice == "3":
        transaction_type = "Expense"
        add_transaction(transactions_list, transaction_type)
    elif choice == "4":
        calculate_balance(transactions_list)
    elif choice == "5":
        spending_by_category(transactions_list)
    elif choice == "6":
        monthly_summary(transactions_list)
    elif choice == "7":
        category = input("Enter the category: ")
        search_transactions(transactions_list, category)
    elif choice == "8":
        if transactions_list:
            save_to_file(transactions_list, filename)
        print("Thank you for using Personal Finance Tracker!")
        print("Good bye")
        break
    else:
        print("Enter the valid choice(1-8)!")