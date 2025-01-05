from __future__ import annotations
from abc import ABC, abstractmethod

class LaptopBuilder(ABC):

    _laptop = None

    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def build_os(self) -> None:
        pass

    @abstractmethod
    def build_cpu(self) -> None:
        pass

    @abstractmethod
    def build_gpu(self) -> None:
        pass

    @abstractmethod
    def get_laptop(self) -> Laptop:
        pass

class Laptop:
    os = None
    cpu = None
    gpu = None

    def __str__(self):
        return f"OS: {self.os}, CPU: {self.cpu}, GPU: {self.gpu}"

class Macbook(Laptop):
    pass

class Asus(Laptop):
    pass

class MacbookBuilder(LaptopBuilder):

    def __init__(self):
        self._laptop = Macbook()

    def reset(self):
        self._laptop.os = "Big Sur"
        self._laptop.cpu = "M1"
        self._laptop.gpu = None
    
    def build_os(self, os="Big Sur"):
        self._laptop.os = os
    
    def build_cpu(self, cpu="M1"):
        self._laptop.cpu = cpu
    
    def build_gpu(self, gpu=None):
        self._laptop.gpu = gpu
    
    def get_laptop(self):
        return self._laptop
    
class AsusBuilder(LaptopBuilder):
    
    def __init__(self):
        self._laptop = Asus()

    def reset(self):
        self._laptop.os = "Windows 10"
        self._laptop.cpu = "AMD Ryzen"
        self._laptop.gpu = "Nvidia"
    
    def build_os(self, os="Windows 10"):
        self._laptop.os = "Windows 10"
    
    def build_cpu(self, cpu="AMD Ryzen"):
        self._laptop.cpu = "AMD Ryzen"
    
    def build_gpu(self, GPU="Nvidia"):
        self._laptop.gpu = "Nvidia"
    
    def get_laptop(self):
        return self._laptop
    
class Director:
    _builder = None

    def __init__(self, builder: LaptopBuilder):
        self._builder = builder
    
    def change_builder(self, builder: LaptopBuilder):
        self._builder = builder