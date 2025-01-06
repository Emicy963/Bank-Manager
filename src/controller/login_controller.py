import bcrypt
from ..model.customer import Customer
from adm_controller import Controller

class Login(Controller):
    def __init__(self) -> None:
        super().__init__()
        
    def __verify_password(self, bi:str, password: str) -> bool:
        customer = self.find_customer(bi)
        if customer:
            return bcrypt.checkpw(password.encode("utf-8"), customer.password)
        return False
    
    def user_login(self, user:Customer) -> Customer | None:
        return user
    
    def login(self, bi:str, password:str) -> bool:
        customer = self.__verify_password(bi, password)
        if customer:
            self.user_login(self.find_customer(bi))
            return True
        return False
