from Assignment.UTIL.DBCONNECTION import DBConnection
from Assignment.ENTITY.ICUSTOMERSERVICEPROVIDER import i_customer_service
from Assignment.DAO.ACCOUNT import Account
from Assignment.DAO.TRANSACTION import Transaction


class cust_service_provider_impl(i_customer_service, Account, DBConnection):
    def get_account_balance(self):
        account = Account()
        self.acc_num = int(input("Enter the account number: "))
        if account.account_exists(self.acc_num):
            res = account.get_account_balance()
            print(res)

    def get_account_details(self):
        account = Account()
        self.acc_num = int(input("Enter the account number: "))
        query = f'select * from Account where acc_num = {self.acc_num}'
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(query)
        data = stmt.fetchall()
        for i in data:
            print(i)
        print("Account details displayed successfully")

    def deposit(self):
        account = Account()
        self.acc_num = int(input("Enter the account number: "))
        amount = float(input("Enter the amount to deposit: "))
        balance = account.fetch(self.acc_num)
        print(balance)
        if amount > 0:
            balance += amount
            account.update_balance(balance, self.acc_num)
            print(f"Deposit successful. Total balance = {balance}")
            transaction = Transaction()
            transaction.acc_num = self.acc_num
            transaction.description = "Deposit"
            transaction.transaction_date = input("Enter the transaction date: ")
            transaction.transaction_type = "Deposit"
            transaction.transaction_amount = amount
            transaction.insert_into()
        else:
            print("Invalid deposit amount")

    def withdraw(self):
        account = Account()
        self.acc_num = int(input("Enter the account number: "))
        amount = float(input("Enter the amount to withdraw: "))
        balance = account.fetch(self.acc_num)
        if (amount > 0) and (amount <= balance):
            balance -= amount
            account.update_balance(balance, self.acc_num)
            print(f"Withdraw successful. Total balance = {balance}")
            transaction = Transaction()
            transaction.acc_num = self.acc_num
            transaction.description = "Withdraw"
            transaction.transaction_date = input("Enter the transaction date: ")
            transaction.transaction_type = "Withdraw"
            transaction.transaction_amount = amount
            transaction.insert_into()
        else:
            print("Invalid Withdrawal amount")

    def transfer(self):
        account = Account()
        sender_num = int(input("Enter the sender account number: "))
        receiver_num = int(input("Enter the receiver account number: "))
        amount = float(input("Enter the amount to transfer: "))
        sender_bal = account.fetch(sender_num)
        receiver_bal = account.fetch(receiver_num)
        if (amount > 0) and (amount <= sender_bal):
            sender_bal -= amount
            receiver_bal += amount
            account.update_balance(sender_bal, sender_num)
            account.update_balance(receiver_bal, receiver_num)
            print("Transfer successful")
            transaction = Transaction()
            transaction.acc_num = self.acc_num
            transaction.description = "Transfer"
            transaction.transaction_date = input("Enter the transaction date: ")
            transaction.transaction_type = "Transfer"
            transaction.transaction_amount = amount
            transaction.insert_into()
        else:
            print("invalid amount")






