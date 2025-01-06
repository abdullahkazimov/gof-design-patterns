from __future__ import annotations
from abc import ABC, abstractmethod

class BankInterface(ABC):

    @abstractmethod
    def operation(self) -> None:
        pass

class RealBank(BankInterface):

    def operation(self):
        print("Real Bank doing some stuff")

class BankProxy(BankInterface):
    
    def __init__(self, authenticated: bool, real_bank: RealBank):
        self.authenticated = authenticated
        self.real_bank = real_bank
    
    def operation(self):
        if self.authenticated:
            self.real_bank.operation()
        else:
            print("Sorry, Bank is not available right now.")
