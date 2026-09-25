from data import accounts
from validation import read_amount, read_text


def deposit_money():
    accnum=read_text("Enter Account Number: ")

    if accnum not in accounts:
        print("Account Not Found.")
        return

    amount=read_amount("Enter Deposit Amount: Rs. ")
    accounts[accnum]["balance"]=accounts[accnum]["balance"]+amount
    accounts[accnum]["transactions"].append("Deposited Rs. " + str(amount))
    print("Money Deposited Successfully.")


def withdraw_money():
    accnum=read_text("Enter Account Number: ")

    if accnum not in accounts:
        print("Account Not Found.")
        return

    amount=read_amount("Enter Withdrawal Amount: Rs. ")

    if amount>accounts[accnum]["balance"]:
        print("Insufficient Balance.")
        return

    accounts[accnum]["balance"]=accounts[accnum]["balance"]-amount
    accounts[accnum]["transactions"].append("Withdrawn Rs. " + str(amount))
    print("Money Withdrawn Successfully.")









    
