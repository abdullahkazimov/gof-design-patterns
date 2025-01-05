from __future__ import annotations
from abc import ABC, abstractmethod
import copy

class Prototype(ABC):
    @abstractmethod
    def get_cpu(self):
        pass

    @abstractmethod
    def clone(self) -> Prototype:
        pass

    @abstractmethod
    def deep_clone(self) -> Prototype:
        pass

class Phone(Prototype):
    def __init__(self, cpu):
        self.cpu = cpu

    def get_cpu(self):
        return self.cpu
    
    def clone(self):
        return copy.copy(self)
    
    def deep_clone(self):
        return copy.deepcopy(self)
    
    def __str__(self):
        return f"CPU: {self.cpu}"
    
class PrototypeRegistry:
    _items = {}

    def add_item(self, id: str, p: Prototype):
        self._items[id] = p
    
    def get_item_clone(self, id: str):
        return self._items[id].clone()
    
    def get_item_deep_clone(self, id: str):
        return self._items[id].deep_clone()
    
    