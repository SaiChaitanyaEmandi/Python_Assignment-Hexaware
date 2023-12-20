from abc import ABC, abstractmethod


class i_customer_service(ABC):

    @abstractmethod
    def get_account_balance(self):
        pass

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass

    @abstractmethod
    def transfer(self):
        pass

    @abstractmethod
    def get_account_details(self):
        pass
