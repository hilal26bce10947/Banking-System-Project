# Banking System

## Overview
The Simple Banking System is a console-based Python application that helps users perform basic banking operations. Users can create accounts, deposit money, withdraw money, check account balances, view transaction details, display account details, show all available accounts, and delete an account with confirmation.

The project uses Python functions, dictionaries, lists, loops, conditional statements, modules, and input validation. Account information is stored temporarily in a dictionary while the program is running. The project is divided into separate Python files for account management, banking operations, reports, validation, and data storage.


## Features Used in this Project
Here, Users can do the following:

1) Create a new account
2) Deposit money
3) Withdraw money
4) Check account balance
5) View transaction details
6) View one account or all accounts
7) Delete an account after confirmation from user


## Technologies Used in this Project
Python 3, Python dictionary, list, functions, loops, conditional statements, and exception handling


## Files Contained in this Project

1) `main.py` - This is the main point which shows the menu and control the programs.
2) `account.py` - This Creates and deletes accounts of users.
3) `banking.py` - This Deposit and Withdraws money.
4) `reports.py` - This Shows balances, accounts, and transactions.
5) `validation.py` - This Validates user input.
6) `data.py` - This Stores account data while the program is running.


## Steps to install & run the project
1) Install Python 3.
2) Download this repository.
3) Open a terminal inside the project folder.
4) Run the command below:
```bash
python main.py
```


## Instructions for testing
Test account creation, duplicate accounts, deposits, withdrawals, insufficient balance, invalid input, account details, and account deletion by entering different types of datas then check outputs are as expected or not. If outputs are as expected then program can run without fail and passed the test. If give error or wierd output then there is a mistake in source code.

These are the following instructions which should be kept in mind to pass the test:
1) If user entered value iss found repeated then it should displays "Account Already exists".
2) If the user enters letters instead of a numeric amount, the program displays an error message instead of stopping.
3) It should checks whether an account exists before performing an operation.
4) It should accepts only positive amounts for deposits, withdrawals, and opening balances.
5) The withdrawal function should prevents the user from withdrawing an amount greater than the available balance.



