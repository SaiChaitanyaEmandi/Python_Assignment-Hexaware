from Assignment.DAO.ACCOUNT import Account


class current_account(Account):
    overdraft_limit = 500

    def __init__(self, overdraft_limit=None):
        super().__init__(None, 'Current', 0.0, 2)
        self.overdraft_limit = overdraft_limit if overdraft_limit is not None else self.overdraft_limit

    def withdraw(self):
        amount = float(input("Enter the amount to withdraw: "))
        if (amount > 0) and (self.acc_bal - amount) >= -self.overdraft_limit:
            self.acc_bal -= amount
            print(f"Withdrew ${amount}. New balance: ${self.acc_bal}")
        else:
            print("Insufficient funds or exceeding overdraft limit.")
