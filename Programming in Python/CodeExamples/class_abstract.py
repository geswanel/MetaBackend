from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def donation(self):
        pass

class Donation(Employee):
    def donation(self):
        a = input("How much do you want to donate: ")
        return a

john = Donation()
print(john.donation())