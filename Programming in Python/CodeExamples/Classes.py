class Alpha:
    c = 10

    def __init__(self):
        self.pub = 3
        self._prot = 2
        self.__pri = 3  # Encapsulation
    
    def get_pri(self):
        return self.__pri


a = Alpha() # instantiation
print(Alpha.c, a.c) # attribute reference

a._prot = 5    # not strict access control
print(a._prot)
print(a.get_pri())  # method reference (self)
print(a._Alpha__pri) # data mangling

class Beta(Alpha):  # Inheritance
    def __init__(self):
        super().__init__()
        self.bpub = -10

b = Beta()
print(b.bpub, b.pub, b._prot)

from abc import ABC

class AbstractExample(ABC): # Abstraction
    pass

# Reusability

class Dish():
    def __init__(self, name, items, time) -> None:
        self.name = name
        self.items = items
        self.time = time
    

    def contents(self):
        print(f"The {self.name} consist of {self.items} and take {self.time} minutes to cook")


pizza = Dish("Pizza", ["cheese", "bread"], 45)
pasta = Dish("Pasta", ["cheese", "pasta"], 55)
print(pizza.time, pasta.time)
print(pizza.contents())

# Inheritance

class Employee():
    def __init__(self, name, last) -> None:
        self.name = name
        self.last = last

class Supervisor(Employee):
    def __init__(self, name, last, password) -> None:
        super().__init__(name, last)    # accessing parent class instance
        self.password = password
    

class Chef(Employee):
    def request_days(self, n):
        return f"{n} days was requested by {self.name}"

adrian = Employee("Adrian", "Smith")

emily = Supervisor("Emily", "Black", "123456")
john = Chef("John", "White")
emily.name = "Emily changed"
print(adrian.name, emily.name)
print(john.request_days(5))