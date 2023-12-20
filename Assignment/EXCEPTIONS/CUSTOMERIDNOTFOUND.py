class customer_id_not_found_exception(Exception):
    def __init__(self, msg="customer id not found"):
        self.msg = msg
        super().__init__(msg)

