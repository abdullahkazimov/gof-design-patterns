from abc import ABC, abstractmethod

class SupportHandler(ABC):
    """
    Abstract base class for all handlers in the chain.
    Each handler has a reference to the 'next' handler in the chain.
    """
    def __init__(self, next_handler=None):
        self._next_handler = next_handler

    def set_next(self, handler):
        """Set the next handler in the chain."""
        self._next_handler = handler

    @abstractmethod
    def handle_ticket(self, severity, message):
        """
        Attempt to handle a support ticket based on severity.
        If it cannot handle, pass to the next handler if available.
        """
        pass


class Tier1Support(SupportHandler):
    """Tier 1 handles simple issues up to severity 3."""
    def handle_ticket(self, severity, message):
        if severity <= 3:
            print(f"Tier1Support: Handling ticket (Severity: {severity}) - {message}")
        else:
            print(f"Tier1Support: Can't handle severity {severity}. Passing to Tier 2.")
            if self._next_handler:
                self._next_handler.handle_ticket(severity, message)


class Tier2Support(SupportHandler):
    """Tier 2 handles issues up to severity 6."""
    def handle_ticket(self, severity, message):
        if severity <= 6:
            print(f"Tier2Support: Handling ticket (Severity: {severity}) - {message}")
        else:
            print(f"Tier2Support: Can't handle severity {severity}. Passing to Tier 3.")
            if self._next_handler:
                self._next_handler.handle_ticket(severity, message)


class Tier3Support(SupportHandler):
    """Tier 3 can handle anything up to severity 10."""
    def handle_ticket(self, severity, message):
        if severity <= 10:
            print(f"Tier3Support: Handling ticket (Severity: {severity}) - {message}")
        else:
            print(f"Tier3Support: Severity {severity} is beyond our capabilities. Escalating further!")

