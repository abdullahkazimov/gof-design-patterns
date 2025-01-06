from __future__ import annotations
from abc import ABC, abstractmethod

class PaymentPlatform(ABC):

    @abstractmethod
    def process_payment(self) -> str:
        pass

class WebPlatform(PaymentPlatform):

    def process_payment(self) -> str:
        return "Paid through web app"

class MobilePlatform(PaymentPlatform):

    def process_payment(self) -> str:
        return "Paid through mobile app"

class PaymentMethod(ABC):
    def __init__(self, platform: PaymentPlatform):
            self.platform = platform
    
    @abstractmethod
    def pay(self) -> None:
        pass

class CashPayment(PaymentMethod):

    def pay(self):
        print(f"Cash Payment Status: {self.platform.process_payment()}")

class CardPayment(PaymentMethod):
    
    def pay(self):
        print(f"Card Payment Status: {self.platform.process_payment()}")