from abc import ABC, abstractmethod

from character_creation.Character import *


# Abstract Factor implementation

# Implement that abstract character background creator
class BackgroundCreator(ABC):
    # initiate the class of type BackgroundCreator
    @abstractmethod
    def __init__(self, background):
        self.background = background
        self.money_amount = None

    # get the chosen background
    @abstractmethod
    def _get_background(self):
        return self.background

    # set the amount of money according to the chosen background
    @abstractmethod
    def _set_money_amount(self, character):
        pass

    # set the background modifying all characteristics specified in background
    @abstractmethod
    def set_background(self, character):
        character.background = self._get_background()
        self._set_money_amount(character)


# Implement the concrete Archeologist background creator
class Archaeologist(BackgroundCreator):
    # implement abstract methods from BackgroundCreator class
    def __init__(self, background):
        super().__init__(background)
        self.money_amount = 25

    def _get_background(self):
        background = super()._get_background()
        return background

    def _set_money_amount(self, character):
        character.money_amount = self.money_amount

    def set_background(self, character):
        super().set_background(character)


# Implement the concrete Golgari agent background creator
class GolgariAgent(BackgroundCreator):
    # implement abstract methods from BackgroundCreator class
    def __init__(self, background):
        super().__init__(background)
        self.money_amount = 10

    def _get_background(self):
        background = super()._get_background()
        return background

    def _set_money_amount(self, character):
        character.money_amount = self.money_amount

    def set_background(self, character):
        super().set_background(character)


# Set the background according to the chosen background
class BackgroundSetter:
    # initiate the setter
    def __init__(self, background):
        self.background = background
        self.character = Character()
        self.character_background = self.__get_background()

    # get the background according to the user input
    def __get_background(self):
        if self.background.upper() == 'ARCHEOLOGIST':
            return Archaeologist(self.background)
        elif self.background.upper() == 'GOLGARI AGENT':
            return GolgariAgent(self.background)

    # commit all modifications that come with the background
    def set_background(self):
        self.character_background.set_background(self.character)
