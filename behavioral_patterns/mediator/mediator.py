class ChatRoom:
    """Mediator class that handles message exchange among participants."""
    
    def __init__(self):
        # Holds a list of registered participants
        self.participants = []

    def register(self, participant):
        """Register a new participant in the chat room."""
        self.participants.append(participant)

    def send(self, message, sender):
        """
        Send a message from the sender to all other participants.
        The sender does not receive the message.
        """
        for participant in self.participants:
            if participant != sender:
                participant.receive(message, sender)


class Participant:
    """Represents a user who sends and receives messages via the chat room."""
    
    def __init__(self, name, chat_room):
        self.name = name
        self.chat_room = chat_room
        # Upon creation, each participant registers with the chat room (the mediator)
        self.chat_room.register(self)

    def send(self, message):
        """Send a message to other participants via the chat room."""
        print(f'{self.name} sends: {message}')
        self.chat_room.send(message, self)

    def receive(self, message, sender):
        """Receive a message from another participant."""
        print(f'{self.name} received from {sender.name}: {message}')