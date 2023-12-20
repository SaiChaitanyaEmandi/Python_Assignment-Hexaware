class overdraft_limit_exceeded_exception(Exception):
    def __init__(self, msg="Overdraft limit exceeded"):
        self.msg = msg
        super().__init__(msg)

