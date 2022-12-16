from character_creation.Character import *


# Strategy Pattern
# Compositor
class MoralAxis:
    def __init__(self, life_strategy=None):
        self.moral_axis = 'neutral'
        self.life_strategy = life_strategy

    def __get_moral_axis(self):
        if self.life_strategy:
            self.moral_axis = self.life_strategy(self)
        else:
            self.moral_axis = 'true-neutral'
        return self.moral_axis

    def set_moral_axis(self):
        morality = self.__get_moral_axis()
        character = Character()
        character.moral_axis = morality


# Concrete Strategy
class Lawful:
    @staticmethod
    def set_moral_axis(moral_axis):
        return 'lawful-' + moral_axis.moral_axis


# Concrete Strategy
class Chaotic:
    @staticmethod
    def set_moral_axis(moral_axis):
        return 'chaotic-' + moral_axis.moral_axis
