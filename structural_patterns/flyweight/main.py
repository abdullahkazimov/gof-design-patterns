from flyweight import Font, Character

font1 = Font("TNR", 12)
font2 = Font("TNR", 12)
font3 = Font("Arial", 12)

char1 = Character(font1)
char2 = Character(font2)

print(char1.font is char2.font) # True