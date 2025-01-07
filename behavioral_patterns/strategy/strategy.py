from abc import ABC, abstractmethod

class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self) -> None:
        pass

class PaypalPayment(PaymentStrategy):
    def pay(self):
        print("PayPal operation")

class VisaPayment(PaymentStrategy):
    def pay(self):
        print("Visa operation")

class Context:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self.strategy = strategy
    
    def run(self):
        self.strategy.pay()
        print("pay() is successful!")