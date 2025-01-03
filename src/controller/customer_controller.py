from ..model.customer import Customer
import bcrypt

class Controller:
    def __init__(self):
        self.customers = []

    def encrypt_password(self, password:str): 
        password_bytes = password.encode("utf-8")
        salt = bcrypt.gensalt()
        password_hash = bcrypt.hashpw(password_bytes, salt)
        return password_hash

    def create_customer(
            self, name:str, password:str, bi:str, amount:int, living:str, age:int, job:str, status:bool)->Customer:
        if not name or not bi:
            raise ValueError("Nome e BI são obrigatórios.")
        if age<0:
            raise ValueError("Idade não pode ser negativa.")
        
        if len(self.customers) != 0:
            for customer in self.customers:
                if customer.bi == bi:
                    raise ValueError("Esse BI já foi cadastrado.")
                
        if amount<10000:
            raise ValueError("Deve depositar ao menos 10.000Kzs para abrir a conta.")
        pin = self.encrypt_password(password)
                
        new_customer = Customer(name, pin, bi, amount, living, age, job, status)
        self.customers.append(new_customer)
        return new_customer
    
    def update_customer(self, name:str=None, bi:str=None, living:str=None, age:int=None, job:str=None)->bool:
        for customer in self.customers:
            if customer.bi == bi:
                if name is not None:
                    customer.name(name)
                if living is not None:
                    customer.living(living)
                if age is not None:
                    customer.age(age)
                if job is not None:
                    customer.job(job)
                return True
        return False

    
    def read_customer(self):
        return self.customers
    
    def find_customer(self, bi:str)-> Customer | None:
        for customer in self.customers:
            if customer.bi == bi:
                return customer
        return None
    
    def delete_customer(self, bi:str)->bool:
        customer = self.find_customer(bi)
        if customer:
            self.customers.append(customer)
            return True
        return False
        
