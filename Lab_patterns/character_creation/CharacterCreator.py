from copy import deepcopy

from character_creation.Character import *
from character_creation.ClassCreator import *
from character_creation.RaceCreator import *
from character_creation.PersonalityCreator import *
from character_creation.ModifierSetter import *
from character_creation.BackgroundCreator import *
from character_creation.UserInteraction import *
from character_creation.CharacterAppearance import *
from character_creation.CharacterGeneralInformation import *


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
        self.__set_character_general_info(name, class_name, race_name, background)
        self.__set_modifiers(modifiers)
        self.__set_traits(traits)
        self.__set_ideals(ideals)
        self.__set_bonds(bonds)
        self.__set_flaws(flaws)
        self.__set_saving_throws(saving_throws)
        self.__set_character_appearance()

    # set the general character's data
    def __set_character_general_info(self, name, class_name, race_name, background):
        general_info_setter = CharacterGeneralInformation(self.character, name, class_name, race_name, background)
        general_info_setter.get_character_general_data()

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

    def __set_character_appearance(self):
        Hair(Skin(Eyes(Weight(Height(Age(CharacterAppearance(self.character))))))).render()

    # show the character instances
    def show_character(self):
        # get the character instances
        character_fields = deepcopy(self.character.__dict__)
        character_fields.pop('_Character__initialized')
        # output the character instances
        print(character_fields)
