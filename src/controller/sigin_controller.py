from adm_controller import Controller
from login_controller import Login
from ..model.customer import Customer

class Sing(Controller):
    def __init__(self):
        super().__init__()

    def singin(self, name:str, password:str, bi:str, amount:int, 
            living:str, age:int, job:str, status:bool) -> Customer | None:
        
        new_customer = self.create_customer(name, password, bi, amount,
                                            living, age, job, status)
        
        login = Login()
        if login.login(bi, password):
            return new_customer
        
        return None