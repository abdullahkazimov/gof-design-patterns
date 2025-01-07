from abc import ABC, abstractmethod

class Subscriber(ABC):
    @abstractmethod
    def update(self, msg) -> None:
        pass

class StandardSubscriber(Subscriber):
    def update(self, msg):
        print(f"New message for Standard Subscriber: {msg}")

class PremiumSubscriber(Subscriber):
    def update(self, msg):
        print(f"New message for Premium Subscriber: {msg}")

class NetflixStream:
    def __init__(self):
        self._subscribers = []

    def add_subscriber(self, subscriber: Subscriber):
        self._subscribers.append(subscriber)
    
    def remove_subscriber(self, subscriber: Subscriber):
        self._subscribers.remove(subscriber)
    
    def notify_subscribers(self):
        for subscriber in self._subscribers:
            subscriber.update("Squid Game 2 is out!")
