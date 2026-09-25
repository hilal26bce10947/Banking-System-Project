# Problem Statement
In daily life, managing banking information such as account details, deposits, withdrawals, and balances is an important task. When this information is handled manually, it can become difficult to keep track of transactions and current balances. A user may forget how much money was deposited or withdrawn, which can lead to calculation errors.

The Simple Banking System is a console-based Python project developed to solve this basic problem. It allows users to manage account information through a menu-driven program. The user can create an account by entering an account number, account holder name, and opening balance. After an account is created, the user can deposit money, withdraw money, check the current balance, view account details, view transaction details, display all accounts, and delete an account.

The project uses a dictionary to store account information. Each account number is used as a unique key, and the account holder name, balance, and transaction list are stored as values. A list is used to record basic transaction messages such as opening balance, deposit amount, and withdrawal amount.


## Scope of the Project
The project supports account creation, deposits, withdrawals, balance checking, account reports, transaction reports, and account deletion. It is made foe acamedic project and is not a real banking application.

The scope of the project includes basic banking operations written are as follows:
1) Create a new account
2) Store account holder name and opening balance
3) Deposit money into an existing account
4) Withdraw money from an existing account
5) Check the current balance
6) Display transaction details
7) Display details of one account
8) Display details of all accounts
9) Delete an account after user confirmation


## Target Users
1) This project is designed mainly for students and beginners who are learning Python programming concepts. It help students how to use functions, modules, dictionaries, lists, loops, conditional statements, exception handling, and input validation im a practical application.
2) Students learning Python programming


## High-Level Features
1) Account management
2) Money deposit and withdrawal
3) Transaction recording
4) Account reporting
5) The system also includes basic validation. It does not allow empty account numbers or names. It checks whether an account exists before performing an operation. It accepts only positive amounts for deposits, withdrawals, and opening balances. If the user enters letters instead of a numeric amount, the program displays an error message instead of stopping unexpectedly. The withdrawal function also prevents the user from withdrawing an amount greater than the available balance.
