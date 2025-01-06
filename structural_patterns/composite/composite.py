from __future__ import annotations
from abc import ABC, abstractmethod

class F1Player(ABC):

    @abstractmethod
    def display(self) -> str:
        pass

class F1Driver(F1Player):

    def __init__(self, name):
        self.name = name

    def display(self):
        return f"Driver name: {self.name}"

class F1Team(F1Player):

    def __init__(self, name):
        self.items = []
        self.name = name

    def add_item(self, player: F1Player):
        self.items.append(player)

    def display(self):
        result = f"Team: {self.name}"
        for item in self.items:
            result += "\n\t" + item.display()
        return result
