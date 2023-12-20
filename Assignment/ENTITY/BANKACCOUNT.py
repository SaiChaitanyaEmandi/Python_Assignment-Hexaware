from abc import ABC, abstractmethod


class BankAccount:
    def __init__(self, acc_no=None, cust_name=None, bal=0.0):
        self.acc_no = acc_no
        self.cust_name = cust_name
        self.bal = bal

    def get_account_number(self):
        return self.acc_no

    def get_customer_name(self):
        return self.cust_name

    def get_balance(self):
        return self.bal

    def set_account_number(self, acc_no):
        self.acc_no = acc_no

    def set_customer_name(self, cust_name):
        self.cust_name = cust_name

    def set_balance(self, bal):
        self.bal = bal

    def print_info(self):
        print(f"Account Number: {self.acc_no}")
        print(f"Customer Name: {self.cust_name}")
        print(f"Balance: {self.bal}")

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def calc_interest(self):
        pass