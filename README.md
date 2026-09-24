'''
# Python-Project

accounts = {}

def create_account():
    accnum = input("Enter Account Number: ")
    if accnum in accounts:
        print("Account already exists.")
    else:
        name = input("Enter Account Holder Name: ")
        balance = float(input("Enter opening Balance: "))
        accounts[accnum] = {"name": name, "balance": balance, "transactions": []}
        print("Account created successfully.")
    '''

