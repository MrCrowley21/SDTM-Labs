from abc import ABC, abstractmethod


# Builder Implementation
# Implementation of abstract method of personality characteristic creator
class PersonalityCreator(ABC):
    # abstract method to get the personality characteristic
    @abstractmethod
    def get_personality_characteristic(self, characteristic):
        pass


# Implementation of concrete class of traits that implements the PersonalityCreator
class PersonalityTraits(PersonalityCreator):
    def get_personality_characteristic(self, traits):
        return traits

    # get the name of the characteristic
    def __str__(self):
        return 'Personality Traits'


# Implementation of concrete class of ideals that implements the PersonalityCreator
class Ideals(PersonalityCreator):
    def get_personality_characteristic(self, ideals):
        return ideals

    # get the name of the characteristic
    def __str__(self):
        return 'Ideals'


# Implementation of concrete class of bonds that implements the PersonalityCreator
class Bonds(PersonalityCreator):
    def get_personality_characteristic(self, bonds):
        return bonds

    # get the name of the characteristic
    def __str__(self):
        return 'Bonds'


# Implementation of concrete class of flaws that implements the PersonalityCreator
class Flaws(PersonalityCreator):
    def get_personality_characteristic(self, flaws):
        return flaws

    # get the name of the characteristic
    def __str__(self):
        return 'Flaws'
