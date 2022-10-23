from copy import deepcopy

from character_creation.Character import *
from character_creation.ClassCreator import *
from character_creation.RaceCreator import *
from character_creation.PersonalityCreator import *
from character_creation.ModifierSetter import *
from character_creation.BackgroundCreator import *
from character_creation.UserInteraction import *


class CharacterCreator:
    # initialize the creator
    def __init__(self):
        self.character = Character()
        self.user_input = UserInteraction()

    def create_character(self):
        # get the user input characteristics
        name, class_name, race_name, background, characteristics, traits, ideals, bonds, flaws = \
            UserInteraction().get_user_input()
        # check if the value for general characteristics were introduced correctly
        if len(characteristics) != len(self.character.characteristics):
            raise Exception('You introduced characteristics wrongly')
        else:
            self.__set_characteristics(characteristics)
        # initiate character modifiers
        modifiers = ModifierSetter()
        # initiate character saving throws
        saving_throws = modifiers.clone()
        # set all instances of the character
        self.__set_character_name(name)
        self.__set_class(class_name)
        self.__set_race(race_name)
        self.__set_background(background)
        self.__set_modifiers(modifiers)
        self.__set_traits(traits)
        self.__set_ideals(ideals)
        self.__set_bonds(bonds)
        self.__set_flaws(flaws)
        self.__set_saving_throws(saving_throws)

    # set the name of the character
    def __set_character_name(self, name):
        self.character.name = name

    # set the class of the character
    def __set_class(self, class_name):
        class_setter = ClassSetter(class_name)
        class_setter.set_character_class()

    # set the race of the character
    def __set_race(self, race_name):
        race_setter = RaceSetter(race_name)
        race_setter.set_race()

    # set the background of the character
    def __set_background(self, background):
        background_setter = BackgroundSetter(background)
        background_setter.set_background()

    # set the traits of the character
    def __set_traits(self, traits):
        trait_setter = PersonalityTraits()
        self.character.personality_characteristics[trait_setter.__str__()] = \
            trait_setter.get_personality_characteristic(traits)

    # set the ideals of the character
    def __set_ideals(self, ideals):
        ideals_setter = Ideals()
        self.character.personality_characteristics[ideals_setter.__str__()] = \
            ideals_setter.get_personality_characteristic(ideals)

    # set the bonds of the character
    def __set_bonds(self, bonds):
        bond_setter = Bonds()
        self.character.personality_characteristics[bond_setter.__str__()] = \
            bond_setter.get_personality_characteristic(bonds)

    # set the flaws of the character
    def __set_flaws(self, flaws):
        flaws_setter = Flaws()
        self.character.personality_characteristics[flaws_setter.__str__()] = \
            flaws_setter.get_personality_characteristic(flaws)

    # set the general characteristics of the character
    def __set_characteristics(self, chars):
        # modify each characteristic according to the user input
        i = 0
        for char in self.character.characteristics:
            self.character.characteristics[char][0] += int(chars[i])
            i += 1

    # set the modifiers of the charcater
    def __set_modifiers(self, modifier):
        modifiers = modifier.get_modifier()
        for char in modifiers:
            self.character.characteristics[char][1] = modifiers[char]

    # set the saving throws of the character
    def __set_saving_throws(self, saving_throws):
        self.character.saving_throws = saving_throws.get_modifier()

    # show the character instances
    def show_character(self):
        # get the character instances
        character_fields = deepcopy(self.character.__dict__)
        character_fields.pop('_Character__initialized')
        # output the character instances
        print(character_fields)
