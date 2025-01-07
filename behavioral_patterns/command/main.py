from command import Light, TurnOnCommand, TurnOffCommand,RemoteControl

if __name__ == "__main__":
    # Receiver
    living_room_light = Light()

    # Concrete Commands
    turn_on_command = TurnOnCommand(living_room_light)
    turn_off_command = TurnOffCommand(living_room_light)

    # Invoker
    remote = RemoteControl()

    # Client sets "turn on" command
    remote.set_command(turn_on_command)
    remote.press_button()   # Output: "Light is turned ON"

    # Client sets "turn off" command
    remote.set_command(turn_off_command)
    remote.press_button()   # Output: "Light is turned OFF"

    # If no command is set
    remote.set_command(None)
    remote.press_button()   # Output: "No command set for this button!"
