# Python-Project

'''
accounts = {}

def create_account():  
    accnum = input("Enter Account Number: ")
    if accnum in accounts:
        print("Account already exists.")
    else:
        name = input("Enter Account Holder Name: ")
        balance = float(input("Enter opening Balance: "))
        accounts[accnum] = {"name": name, "balance": balance, "transactions": ["Opening Balance: Rs. " + str(balance)]}
        print("Account created successfully.")

def deposit_money():
    accnum = input("Enter Account Number: ")
    if accnum in accounts:
        amount = float(input("Enter Deposit Amount: "))
        accounts[accnum]["balance"] = accounts[accnum]["balance"] + amount
        accounts[accnum]["transactions"].append("Deposited Rs. " + str(amount))
        print("Money Deposited Successfully.")
    else:
        print("Account Not Found.")

def withdraw_money():
    accnum = input("Enter Account Number: ")
    if accnum in accounts:
        amount = float(input("Enter Withdrawal Amount: "))
        if amount <= accounts[accnum]["balance"]:
            accounts[accnum]["balance"] = accounts[accnum]["balance"] - amount
            accounts[accnum]["transactions"].append("Withdrawn Rs. " + str(amount))
            print("Money Withdrawn Successfully.")
        else:
            print("Insufficient  Balance.")
    else:
        print("Account Not Found.")

'''
