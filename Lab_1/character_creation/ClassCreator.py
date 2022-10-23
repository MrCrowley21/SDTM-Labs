from character_creation.Character import *


# Factory Method implementation

# Implementation of class "Bard"
class Bard:
    # initialize class character
    def __init__(self):
        self.chr_name = 'Bard'
        self.characteristic = ['Dexterity', 'Charisma']

    # get the name of the class of the character
    def _get_name(self):
        return self.chr_name

    # set the saving throws according to the class of the character
    def _set_saving_throws(self):
        return self.characteristic


# Implementation of class "Barbarian"
class Barbarian:
    # initialize class character
    def __init__(self):
        self.chr_name = 'Barbarian'
        self.characteristic = ['Strength', 'Constitution']

    # get the name of the class of the character
    def _get_name(self):
        return self.chr_name

    # set the saving throws according to the class of the character
    def _set_saving_throws(self):
        return self.characteristic


# Implementation of class "Fighter"
class Fighter:
    # initialize class character
    def __init__(self):
        self.chr_name = 'Fighter'
        self.characteristic = ['Strength', 'Constitution']

    # get the name of the class of the character
    def _get_name(self):
        return self.chr_name

    # set the saving throws according to the class of the character
    def _set_saving_throws(self):
        return self.characteristic


# Implementation of class "Wizard"
class Wizard:
    # initialize class character
    def __init__(self):
        self.chr_name = 'Wizard'
        self.characteristic = ['Intelligence', 'Wisdom']

    # get the name of the class of the character
    def _get_name(self):
        return self.chr_name

    # set the saving throws according to the class of the character
    def _set_saving_throws(self):
        return self.characteristic


# Implementation of class "Druid"
class Druid:
    # initialize class character
    def __init__(self):
        self.chr_name = 'Druid'
        self.characteristic = ['Intelligence', 'Wisdom']

    # get the name of the class of the character
    def _get_name(self):
        return self.chr_name

    # set the saving throws according to the class of the character
    def _set_saving_throws(self):
        return self.characteristic


# Factory Method
class CharacterClass:
    def __init__(self, class_name):
        self.class_name = class_name

    # get the concrete class of the character
    def get_character_class(self):
        if self.class_name == 'BARD':
            return Bard()
        elif self.class_name == "BARBARIAN":
            return Barbarian()
        elif self.class_name == "FIGHTER":
            return Fighter()
        elif self.class_name == "WIZARD":
            return Wizard()
        elif self.class_name == "DRUID":
            return Druid()
        else:
            print('You introduced a non-valid character class. Please, select a valid character class')


# Class that sets the class name of a character
class ClassSetter:
    # initialize class setter
    def __init__(self, class_name):
        self.character = Character()
        self.class_name = class_name.upper()
        self.chr_class = CharacterClass(self.class_name)

    # set the class of the character by adding its name and saving throws in description
    def set_character_class(self):
        character_class = self.chr_class.get_character_class()
        self.__set_class_name(character_class)
        self.__add_saving_throws(character_class)

    # set the name of the class
    def __set_class_name(self, character_class):
        self.character.chr_class = character_class._get_name()

    # modify saving throws according to the characteristics of the class
    def __add_saving_throws(self, character_class):
        saving_throws = character_class._set_saving_throws()
        for attribute in saving_throws:
            self.character.characteristics[attribute][0] += 1

