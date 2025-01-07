from mediator import ChatRoom, Participant

# --- Usage Example ---
if __name__ == '__main__':
    # Create a mediator (chat room)
    chat_room = ChatRoom()

    # Create participants
    alice = Participant('Alice', chat_room)
    bob = Participant('Bob', chat_room)
    charlie = Participant('Charlie', chat_room)

    # Participants sending messages
    alice.send('Hi everyone!')
    bob.send('Hello Alice!')
    charlie.send('Hey guys!')
