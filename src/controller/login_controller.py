import bcrypt
from ..model.customer import Customer
from adm_controller import Controller

class LoginController:
    def __init__(self):
        self._logged_user = None
        
    def verify_password(self, bi:str, password: str) -> bool:
        customer = Controller()
        if customer:
            return bcrypt.checkpw(password.encode("utf-8"), customer.find_customer(bi).password)
        return False
    
    def login(self, bi:str, password:str) -> bool:
        customer = Controller()
        if self.verify_password(bi, password):
            self._logged_user = customer.find_customer(bi)
            return True
        return False
    
    def get_logged_user(self) -> Customer | None:
        return self._logged_user

    def logout(self) -> None:
        self._logged_user = None

    def singIn(self, name: str, password: str, bi: str, 
              amount: float, living: str, age: int, 
              job: str, status: bool=False):
        new_customer = Controller()
        new_customer.create_customer(name, password, bi, amount, living, age, job, status)
        
        self.login(bi, password)
