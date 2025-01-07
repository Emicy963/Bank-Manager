from adm_controller import Controller
from login_controller import LoginController


class OperationController:
    def __init__(self, logged_user:LoginController):
        self._logged_user = logged_user.get_logged_user()
        self.operations_history = []

    def validation_amount(self, amount:int) -> None:
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        if amount > self._logged_user.amount:
            raise ValueError("Amount Insuficient.")

    def deposit(self, amount:int) -> int:
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        self._logged_user.amount += amount
        return self._logged_user.amount

    def withdraw(self, amount:int) -> int:
        self.validation_amount(amount)
        self._logged_user.amount -= amount
        return self._logged_user.amount
    
    def transfer(self, to_bi:str, amount:int) -> None:
        customer = Controller()
        to_customer = customer.find_customer(to_bi)
        self.validation_amount(amount)
        to_customer += amount
        self._logged_user.amount -= amount

    def check_balance(self) -> int:
        return self._logged_user.amount
