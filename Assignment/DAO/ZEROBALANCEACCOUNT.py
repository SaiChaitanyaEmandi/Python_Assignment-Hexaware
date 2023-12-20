from Assignment.DAO.ACCOUNT import Account


class zero_balance_account(Account):
    def __init__(self):
        super().__init__(None,'Zero Balance', 0.0, 3)
