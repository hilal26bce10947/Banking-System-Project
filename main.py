from account import (create_account, delete_account)
from banking import (deposit_money, withdraw_money)
from reports import (account_details, check_balance, show_all_account_details, transaction_details)


def main():
    while True:
        print()
        print("===== BANKING SYSTEM =====")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction Details")
        print("5. Check Balance")
        print("6. Account Details")
        print("7. Show All Account Details")
        print("8. Delete Account")
        print("9. Exit")
        print()

        choice=input("Enter your choice: ")

        if choice=="1":
            create_account()
            
        elif choice=="2":
            deposit_money()
            
        elif choice=="3":
            withdraw_money()
            
        elif choice=="4":
            transaction_details()

        elif choice=="5":
            check_balance()
            
        elif choice=="6":
            account_details()
            
        elif choice=="7":
            show_all_account_details()
            
        elif choice=="8":
            delete_account()
            
        elif choice=="9":
            print("Thank you")
            break
        
        else:
            print("Invalid choice. Please select a number from 1 to 9.")


main()
