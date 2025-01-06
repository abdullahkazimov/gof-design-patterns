class Font:
    _fonts = {}

    def __new__(cls, font_family, font_size):
        key = (font_family, font_size)
        if key not in cls._fonts:
            cls._fonts[key] = super().__new__(cls)
            cls._fonts[key].font_family = font_family
            cls._fonts[key].font_size = font_size
        return cls._fonts[key]
    
    def __str__(self):
        return f"font family: {self.font_family} | font size: {self.font_size}"

class Character:

    def __init__(self, font: Font):
        self.font = font
    
    def display(self):
        return "this character uses font {self.font}"