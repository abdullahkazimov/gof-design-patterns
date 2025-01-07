from abc import ABC, abstractmethod

class OrderState(ABC):
    @abstractmethod
    def process_order(self, order):
        pass

    @abstractmethod
    def next_state(self, order):
        pass

    @abstractmethod
    def cancel_order(self, order):
        pass

class OrderedState(OrderState):
    def process_order(self, order):
        print("Order placed successfully. Preparing for shipment...")

    def next_state(self, order):
        # Transition to the Shipped state
        print("Order is now shipped.")
        order.state = ShippedState()

    def cancel_order(self, order):
        print("Order canceled successfully.")
        # We could also set order.state to some 'CanceledState' if needed
        order.state = None


class ShippedState(OrderState):
    def process_order(self, order):
        print("Order is already shipped. Processing tracking details...")

    def next_state(self, order):
        # Transition to the Delivered state
        print("Order has been delivered.")
        order.state = DeliveredState()

    def cancel_order(self, order):
        print("Cannot cancel. The order is already shipped!")


class DeliveredState(OrderState):
    def process_order(self, order):
        print("Order already delivered to the customer.")

    def next_state(self, order):
        print("Order is already in its final state (delivered). No further transition.")

    def cancel_order(self, order):
        print("Cannot cancel. The order is already delivered!")

class Order:
    def __init__(self):
        # Initial State = Ordered
        self.state = OrderedState()

    def process(self):
        self.state.process_order(self)

    def next(self):
        self.state.next_state(self)

    def cancel(self):
        self.state.cancel_order(self)
