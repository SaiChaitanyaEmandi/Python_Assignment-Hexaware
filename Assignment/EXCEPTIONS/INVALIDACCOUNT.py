class invalid_account_exception(Exception):
    def __init__(self, msg="Invalid account number"):
        self.msg = msg
        super().__init__()

