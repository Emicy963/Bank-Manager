class Customer:
    def __init__(self, name:str, password:bytes, bi:str, amount:int, living:str, age:int, job:str, status:bool)->None:
        self._name = name
        self._password = password
        self._bi = bi
        self._amount = amount
        self._living = living
        self._age = age
        self._job = job
        self._status = status

    @property
    def name(self)->str:
        return self._name
    @name.setter
    def name(self, name)->None:
        self._name = name

    @property
    def password(self)->bytes:
        return self._password
    @password.setter
    def password(self, password)->None:
        self._password = password

    @property
    def bi(self)->str:
        return self._bi
    @bi.setter
    def bi(self, bi)->None:
        self._bi = bi

    @property
    def amount(self)->int:
        return self._amount
    @amount.setter
    def amount(self, amount)->None:
        self._amount = amount
    
    @property
    def living(self)->str:
        return self._living
    @living.setter
    def living(self, living)->None:
        self._living = living

    @property
    def age(self)->int:
        return self._age
    @age.setter
    def age(self, age)->None:
        self._age = age

    @property
    def job(self)->str:
        return self._job
    @job.setter
    def job(self, job)->None:
        self._job = job

    @property
    def status(self)->bool:
        return self._status
    @status.setter
    def status(self, status)->None:
        self._status = status
