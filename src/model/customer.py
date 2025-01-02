class Customer:
    def __init__(self, name:str, bi:str, living:str, age:int, job:str):
        self.name = name
        self.bi = bi
        self.living = living
        self.age = age
        self.job = job

    @property
    def name(self)->str:
        return self.name
    @name.setter
    def name(self, name):
        self.name = name

    @property
    def bi(self)->str:
        return self.bi
    @bi.setter
    def bi(self, bi):
        self.bi = bi
    
    @property
    def living(self)->str:
        return self.living
    def living(self, living):
        self.living = living

    @property
    def age(self)->int:
        return self.age
    @age.setter
    def age(self, age):
        self.age = age

    @property
    def job(self)->str:
        return self.job
    @job.setter
    def job(self, job):
        self.job = job
