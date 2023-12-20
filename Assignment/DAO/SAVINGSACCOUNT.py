from Assignment.DAO.ACCOUNT import Account


class savings_account(Account):
    def __init__(self, interest_rate):
        super().__init__(None, "Savings", 500 , 1)
        self.interest_rate = interest_rate

    def calc_interest(self):
        interest_amount = self.acc_bal * (self.interest_rate / 100)
        print(f"Interest calculated: ${interest_amount}")


