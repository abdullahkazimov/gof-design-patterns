from abc import ABC, abstractmethod

class Light:
    def turn_on(self):
        print("Light Turned On")
    
    def turn_off(self):
        print("Light Turned Off")

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class TurnOnCommand(Command):
    def __init__(self, light: Light):
        self.light = Light()

    def execute(self):
        self.light.turn_on()
    
class TurnOffCommand(Command):
    def __init__(self, light: Light):
        self.light = Light()

    def execute(self):
        self.light.turn_off()

class RemoteControl:
    def __init__(self):
        self.button_command = None

    def set_command(self, command: Command):
        self.button_command = command

    def press_button(self):
        if self.button_command:
            self.button_command.execute()
        else:
            print("No command set for this button!")
