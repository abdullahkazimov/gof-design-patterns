from __future__ import annotations
from abc import ABC, abstractmethod

class BrandFactory(ABC):

    @abstractmethod
    def create_smartphone(self) -> Phone:
        pass

    @abstractmethod
    def create_laptop(self) -> Laptop:
        pass

class AppleFactory(BrandFactory):
    
    def create_smartphone(self) -> Phone:
        return IPhone()
    
    def create_laptop(self) -> Laptop:
        return Macbook()
    
class SamsungFactory(BrandFactory):
    
    def create_smartphone(self) -> Phone:
        return Galaxy()
    
    def create_laptop(self) -> Laptop:
        return Vaio()

class Phone(ABC):
    
    @abstractmethod
    def call(self):
        pass

class Laptop(ABC):

    @abstractmethod
    def start(self):
        pass

class IPhone(Phone):

    def call(self):
        return "calling using iPhone"

class Galaxy(Phone):

    def call(self):
        return "calling using Galaxy"
    
class Macbook(Laptop):

    def start(self):
        return "starting using Macbook"

class Vaio(Laptop):

    def start(self):
        return "starting using Vaio"

