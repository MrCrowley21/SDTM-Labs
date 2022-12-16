from character_creation.Character import *
from character_creation.ClassCreator import *
from character_creation.RaceCreator import *
from character_creation.PersonalityCreator import *
from character_creation.ModifierSetter import *
from character_creation.BackgroundCreator import *


class UserInteraction:
    # initiate the user input class
    def __init__(self):
        self.class_list = ['BARD', 'BARBARIAN', 'FIGHTER', 'WIZARD', 'DRUID']
        self.race_list = ['AVEN', 'AARAKOCRA', 'BUGBEAR', 'DWARF', 'GOLIATH']
        self.background_list = ['ARCHEOLOGIST', 'GOLGARI AGENT']

    # get all characteristics input by the user
    def get_user_input(self):
        print('Welcome to the D&D character creation helper!')
        name = self.__get_name()
        class_name = self.__get_class_name()
        race_name = self.__get_race_name()
        background = self.__get_background()
        characteristics = self.__get_characteristics()
        traits = self.__get_traits()
        ideals = self.__get_ideals()
        bonds = self.__get_bonds()
        flaws = self.__get_flaws()
        life_strategy = self.__get_life_strategy()
        armor = self.__get_armor()
        return name, class_name, race_name, background, characteristics, traits, ideals, bonds, flaws, \
            life_strategy, armor

    # get character name
    def __get_name(self):
        print('To begin with, introduce a name for your character: ')
        name = input()
        return name

    # get character class name
    def __get_class_name(self):
        print('Great!\nNow, as your character has a name, it is time to choose his/her class. Please, choose '
              'one from the official D&D 5 classes')
        class_name = input()
        while class_name.upper() not in self.class_list:
            print('You introduced a non-valid character class. Please, select a valid character class')
            class_name = input()
        return class_name

    # get character race name
    def __get_race_name(self):
        print('Wow! You are doing really great!\nRight now it is the right time for you to choose the race you are '
              'gonna be! Please, choose one from the official D&D 5 races')
        race_name = input()
        while race_name.upper() not in self.race_list:
            print('You introduced a non-valid character race. Please, select a valid character race')
            race_name = input()
        return race_name

    # get character background
    def __get_background(self):
        print('It is obvious that each person has a history! Tell something about the background of your character!\n'
              'Please, select a valid character background from the official D&D 5 game rules!')
        background = input()
        while background.upper() not in self.background_list:
            print('You introduced a non-valid character background. Please, select a valid character background')
            background = input()
        return background

    # get character general characteristics
    def __get_characteristics(self):
        characteristics = []
        print('You are doing very well!\n'
              'You have six main characteristics: Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma.'
              'You should split the following indexes among them: 8, 10, 11, 12, 13, 14.\n'
              'Please, write the corresponding number in the order of characteristics above, with space between them')
        try:
            characteristics += input().split()
        except:
            raise Exception('The characteristic should be integer number')
        return characteristics

    # get character traits
    def __get_traits(self):
        print('Good job! You are almost done.\nIt is time to write some personality treats you want your character '
              'to have')
        traits = input()
        return traits

    # get character ideals
    def __get_ideals(self):
        print('Alright! What about setting up some ideals for him/her?')
        ideals = input()
        return ideals

    # get character bonds
    def __get_bonds(self):
        print('We like how you are going!\nNow, tell us about some bonds of your character')
        bonds = input()
        return bonds

    # get character bonds
    def __get_flaws(self):
        print('Of course, everyone has flows! Do not be shy and admit the back-draws of your character!')
        flaws = input()
        return flaws

    # get character life strategy
    def __get_life_strategy(self):
        print('Are you rather lawful or chaotic!')
        life_strategy = input()
        return life_strategy

    # get character armor
    def __get_armor(self):
        armor = []
        print('Please, write the armor for head you want!')
        armor.append((input(), 'head'))
        print('Please, write the armor for chest you want!')
        armor.append((input(), 'chest'))
        print('Please, write the armor for hands you want!')
        armor.append((input(), 'hands'))
        return armor
