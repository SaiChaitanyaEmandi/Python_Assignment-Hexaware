from Assignment.DAO.ACCOUNT import Account
from Assignment.DAO.SAVINGSACCOUNT import savings_account
from Assignment.DAO.CURRENTACCOUNT import current_account
from Assignment.DAO.ZEROBALANCEACCOUNT import zero_balance_account


class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, acc_type):
        acc_no = input("Enter account number: ")
        initial_balance = float(input("Enter initial balance: "))

        if acc_type.lower() == "savings":
            interest_rate = float(input("Enter interest rate for savings account: "))
            account = savings_account(acc_no, initial_balance, interest_rate)
        elif acc_type.lower() == "current":
            account = current_account(acc_no, initial_balance)
        else:
            print("Invalid account type.")
            return

        self.accounts.append(account)
        print(f"{acc_type.capitalize()} account created successfully. Account Number: {acc_no}")

    def deposit(self):
        acc_no = input("Enter account number: ")
        amount = float(input("Enter deposit amount: "))

        account = self.find_account(acc_no)
        if account:
            account.deposit(amount)
        else:
            print(f"Account {acc_no} not found.")

    def withdraw(self):
        acc_no = input("Enter account number: ")
        amount = float(input("Enter withdrawal amount: "))

        account = self.find_account(acc_no)
        if account:
            account.withdraw(amount)
        else:
            print(f"Account {acc_no} not found.")

    def calc_interest(self):
        interest_rate = float(input("Enter the interest rate: "))
        acc_no = input("Enter account number: ")
        account = self.find_account(acc_no)
        if account and isinstance(account, savings_account):
            account.calc_interest(interest_rate)
        else:
            print(f"Account {acc_no} not found or not a savings account.")

    def find_account(self, acc_no):
        for account in self.accounts:
            if account.get_account_number() == acc_no:
                return account
        return None

