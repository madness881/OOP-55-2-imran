class BankAccount:
    def __init__(self,user_name,balance,password):
        self.user_name = user_name
        #protecked
        self._balance = balance
        #private
        self.__password = password
    def get_balance(self):
        return self._balance


from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def maпшеke_sound(self):
        ...
    @abstractmethod
    def move(self):
        pass
