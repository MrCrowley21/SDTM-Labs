from character_creation.ClassCreator import *
from character_creation.RaceCreator import *
from character_creation.BackgroundCreator import *


# Facade Method
class CharacterGeneralInformation:
    def __init__(self, character, name, class_name, race, background):
        self.character = character
        self.name = name
        self.class_name = class_name
        self.race = race
        self.background = background

    def __initialize_general_info(self):
        class_setter = ClassSetter(self.class_name)
        race_setter = RaceSetter(self.race)
        background_setter = BackgroundSetter(self.background)
        return class_setter, race_setter, background_setter

    def get_character_general_data(self):
        class_setter, race_setter, background_setter = self.__initialize_general_info()
        self.character.name = self.name
        class_setter.set_character_class()
        race_setter.set_race()
        background_setter.set_background()

