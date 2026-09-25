from data import accounts
from validation import read_text


def check_balance():
    accnum=read_text("Enter Account Number: ")

    if accnum in accounts:
        print("Current Balance: Rs.", accounts[accnum]["balance"])

    else:
        print("Account Not Found.")


def transaction_details():
    accnum=read_text("Enter Account Number: ")

    if accnum not in accounts:
        print("Account Not Found.")
        return
    
    print()
    print("===== TRANSACTION DETAILS =====")

    for i in accounts[accnum]["transactions"]:
        print(i)


def account_details():
    accnum=read_text("Enter Account Number: ")

    if accnum not in accounts:
        print("Account Not Found.")
        return

    print()
    print("===== ACCOUNT DETAILS =====")
    print("Account Number:", accnum)
    print("Account Holder Name:", accounts[accnum]["name"])
    print("Current Balance: Rs.", accounts[accnum]["balance"])


def show_all_account_details():
    if len(accounts)==0:
        print("No Accounts Available.")
        return

    print()
    print("===== ALL ACCOUNT DETAILS =====")

    for i in accounts:
        print()
        print("Account Number:", i)
        print("Account Holder Name:", accounts[i]["name"])
        print("Current Balance: Rs.", accounts[i]["balance"])









        
