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
    
    def find_customer(self, bi:str)-> Customer | None:
        for customer in self.customers:
            if customer.bi == bi:
                return customer
            else:
                raise ValueError("User don't exist!")
        return None
    
    def read_customer(self):
            return self.customers
    
    def create_customer(
            self, name:str, password:str, bi:str, amount:int, living:str, age:int, job:str, status:bool)->Customer:
        if not name or not bi:
            raise ValueError("Name and BI are required.")
        if age<0:
            raise ValueError("Age cannot be negative.")
        
        if len(self.customers) != 0:
            for customer in self.customers:
                if customer.bi == bi:
                    raise ValueError("This BI already exist!")
                
        if amount<10000:
            raise ValueError("Deposit must be greater than 10000Kzs")
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long.")
        if not any(c.isdigit() for c in password):
            raise ValueError("Password must be at least one number.")
        if not any(c.isupper() for c in password):
            raise ValueError("Password must have at least one uppercase letter.")
        
        pin = self.encrypt_password(password)
                
        new_customer = Customer(name, pin, bi, amount, living, age, job, status)
        self.customers.append(new_customer)
        return new_customer
    
    def update_customer(
            self, 
            name:str=None, 
            password:str=None, 
            bi:str=None,
            amount:int=None, 
            living:str=None, 
            age:int=None, 
            job:str=None)->bool:
        
        for customer in self.customers:
            if customer.bi == bi:
                if name is not None:
                    customer.name = name
                if password is not None:
                    if len(password) < 8:
                        raise ValueError("Password must be at least 8 characters long.")
                    if not any(c.isdigit() for c in password):
                        raise ValueError("Password must be at least one number.")
                    if not any(c.isupper() for c in password):
                        raise ValueError("Password must have at least one uppercase letter.")
                    pin = self.encrypt_password(password)
                    customer.password = pin
                if amount is not None:
                    customer.amount = amount
                if living is not None:
                    customer.living = living
                if age is not None:
                    if age<0:
                        raise ValueError("Age cannot be negative.")
                    customer.age = age
                if job is not None:
                    customer.job = job
                return True
        return False

    def delete_customer(self, bi:str)->bool:
        customer = self.find_customer(bi)
        if customer:
            self.customers.append(customer)
            return True
        return False
        
