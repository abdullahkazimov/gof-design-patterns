from __future__ import annotations
from abc import ABC, abstractmethod

class Kitchen(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def operation(self):
        meal = self.factory_method()
        return meal.serve()

class AsianCuisine(Kitchen):
    
    def factory_method(self):
        return Sushi()

class ItalianCuisine(Kitchen):
    
    def factory_method(self):
        return Pizza()

class Meal(ABC):
    @abstractmethod
    def serve(self):
        pass

class Sushi(Meal):
    def serve(self):
        return "Arigato!"

class Pizza(Meal):
    def serve(self):
        return "Forza Pizza es sempre!"