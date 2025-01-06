class TV:
    def turn_on(self):
        pass

class SoundSystem:
    def turn_volume_up(self, percent:int):
        pass

class HomeCinemaFacade:
    def __init__(self):
        self.tv = TV()
        self.sound_system = SoundSystem()

    def start(self):
        self.tv.turn_on()
        self.sound_system.turn_volume_up(100)
        print("Your home cinema is ready now")