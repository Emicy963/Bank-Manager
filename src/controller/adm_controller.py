from ..model.customer import Customer
import bcrypt

class Controller:
    def __init__(self):
        self._customers = []

    def encrypt_password(self, password:str): 
        password_bytes = password.encode("utf-8")
        salt = bcrypt.gensalt()
        password_hash = bcrypt.hashpw(password_bytes, salt)
        return password_hash
    
    def find_customer(self, bi:str)-> Customer | None:
        for customer in self._customers:
            if customer.bi == bi:
                return customer
            else:
                raise ValueError("User don't exist!")
        return None
    
    def validate_customer_data(self, name:str, password:str, bi:str, amount:int, age:int) -> None:
        if not name or not bi:
            raise ValueError("Name and BI are required.")
        if age<0:
            raise ValueError("Age cannot be negative.")
        if age<18:
            raise ValueError("Your age must be greate than 18 years.")
        
        customer = self.find_customer(bi)
        if customer:
            raise ValueError("This BI already Exist!")
                
        if amount<10000:
            raise ValueError("Deposit must be greater than 10000Kzs")
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long.")
        if not any(c.isdigit() for c in password):
            raise ValueError("Password must be at least one number.")
        if not any(c.isupper() for c in password):
            raise ValueError("Password must have at least one uppercase letter.")
    
    def create_customer(
            self, name:str, password:str, bi:str, amount:int, 
            living:str, age:int, job:str, status:bool)->Customer:
        
        self.validate_customer_data(name, password, bi, amount, age)
        encrypted_password = self.encrypt_password(password)
                
        new_customer = Customer(name, encrypted_password, bi, amount, living, age, job, status)
        self._customers.append(new_customer)
        return new_customer
    
    def update_customer(
            self, 
            name:str=None, 
            password:str=None, 
            bi:str=None,
            amount:int=None, 
            living:str=None, 
            age:int=None, 
            job:str=None,
            status:bool=None)->bool:
        customer = self.find_customer(bi)
        if not customer:
            return False
        
        if name:
            customer.name = name
        if password:
            if len(password) < 8:
                raise ValueError("Password must be at least 8 characters long.")
            if not any(c.isdigit() for c in password):
                raise ValueError("Password must be at least one number.")
            if not any(c.isupper() for c in password):
                raise ValueError("Password must have at least one uppercase letter.")
            customer.password = self.encrypt_password(password)
        if amount is not None:
            customer.amount = amount
        if living is not None:
            customer.living = living
        if age is not None:
            if age < 0:
                raise ValueError("Age cannot be negative.")
            customer.age = age
        if job is not None:
            customer.job = job
        if status is not None:
            customer.status = status

        return True

    def delete_customer(self, bi:str)->bool:
        customer = self.find_customer(bi)
        if customer:
            self._customers.remove(customer)
            return True
        return False
        
    def get_all_customers(self):
        return self._customers
