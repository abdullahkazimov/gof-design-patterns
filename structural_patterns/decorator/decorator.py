from __future__ import annotations
from abc import ABC, abstractmethod

class Coffee(ABC):
    
    @abstractmethod
    def ingredients(self) -> str:
        pass

class CoffeeDecorator(Coffee):

    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    def ingredients(self) -> str:
        return self._coffee.ingredients()

class SimpleCoffee(Coffee):

    def ingredients(self):
        return "Caffeein"

class MilkDecorator(CoffeeDecorator):

    def ingredients(self):
        return super().ingredients() + ", Milk"

class SugarDecorator(CoffeeDecorator):

    def ingredients(self):
        return super().ingredients() + ", Sugar"