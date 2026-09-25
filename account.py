from data import accounts
from validation import read_amount, read_text


def create_account():
    accnum=read_text("Enter Account Number: ")

    if accnum in accounts:
        print("Account Already Exists.")
        return

    name=read_text("Enter Account Holder Name: ")
    balance=read_amount("Enter Opening Balance: Rs. ")
    accounts[accnum]={"name": name, "balance": balance, "transactions": ["Opening Balance: Rs. " + str(balance)]}

    print("Account Created Successfully.")


def delete_account():
    accnum=read_text("Enter Account Number to Delete: ")

    if accnum not in accounts:
        print("Account Not Found.")
        return

    answer=input("Are you sure you want to Delete it? (yes/no): ").lower()

    if answer=="yes":
        del accounts[accnum]
        print("Account Deleted Successfully.")
        
    else:
        print("Account Deletion Cancelled.")









        
