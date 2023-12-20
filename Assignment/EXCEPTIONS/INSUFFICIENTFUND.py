class insufficient_fund_exception(Exception):
    def __init__(self, msg="Insufficient funds"):
        self.msg = msg
        super().__init__(msg)
