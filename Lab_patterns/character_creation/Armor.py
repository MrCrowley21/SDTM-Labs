from character_creation.Character import *


# Mediator
class Armor:
    def __init__(self, armor_type):
        self.type = armor_type
        self.character = Character()

    def __str__(self):
        return self.type

    def set_new_armor(self, armor_name):
        self.character.armor.append((self.type, armor_name))
