from abc import ABC, abstractmethod

from character_creation.Character import *


# Abstract Factor implementation

# Implement that abstract character race creator
class RaceCreator(ABC):
    # initiate the class of type RaceCreator
    @abstractmethod
    def __init__(self, race):
        self.race = race

    # get the chosen race type
    @abstractmethod
    def _get_race(self):
        return self.race

    # set the characteristics according to the chosen race
    @abstractmethod
    def _get_characteristics(self, character, characteristics):
        for char in characteristics:
            character.characteristics[char][0] += characteristics[char]

    # set the race modifying all characteristics specified in race
    @abstractmethod
    def set_race(self, character):
        pass


# Implement the concrete Aarakocra race creator
class Aarakocra(RaceCreator):
    # implement abstract methods from RaceCreator class
    def __init__(self, race):
        super().__init__(race)
        self.characteristics = {
            'Dexterity': 2,
            'Wisdom': 1,
        }

    def _get_race(self):
        race = super()._get_race()
        return race

    def _get_characteristics(self, character, characteristics):
        super()._get_characteristics(character, self.characteristics)

    def set_race(self, character):
        character.chr_race = self._get_race()
        self._get_characteristics(character, self.characteristics)


# Implement the concrete Aven race creator
class Aven(RaceCreator):
    def __init__(self, race):
        # implement abstract methods from RaceCreator class
        super().__init__(race)
        self.characteristics = {
            'Dexterity': 2,
        }

    def _get_race(self):
        race = super()._get_race()
        return race

    def _get_characteristics(self, character, characteristics):
        super()._get_characteristics(character, self.characteristics)

    def set_race(self, character):
        character.chr_race = self._get_race()
        self._get_characteristics(character, self.characteristics)


# Implement the concrete Bugbear race creator
class Bugbear(RaceCreator):
    def __init__(self, race):
        # implement abstract methods from RaceCreator class
        super().__init__(race)
        self.characteristics = {
            'Strength': 2,
            'Dexterity': 1,
        }

    def _get_race(self):
        race = super()._get_race()
        return race

    def _get_characteristics(self, character, characteristics):
        super()._get_characteristics(character, self.characteristics)

    def set_race(self, character):
        character.chr_race = self._get_race()
        self._get_characteristics(character, self.characteristics)


# Implement the concrete Dwarf race creator
class Dwarf(RaceCreator):
    def __init__(self, race):
        # implement abstract methods from RaceCreator class
        super().__init__(race)
        self.characteristics = {
            'Complexity': 2,
        }

    def _get_race(self):
        race = super()._get_race()
        return race

    def _get_characteristics(self, character, characteristics):
        super()._get_characteristics(character, self.characteristics)

    def set_race(self, character):
        character.chr_race = self._get_race()
        self._get_characteristics(character, self.characteristics)


# Implement the concrete Goliath race creator
class Goliath(RaceCreator):
    def __init__(self, race):
        # implement abstract methods from RaceCreator class
        super().__init__(race)
        self.characteristics = {
            'Strength': 2,
            'Complexity': 1,
        }

    def _get_race(self):
        race = super()._get_race()
        return race

    def _get_characteristics(self, character, characteristics):
        super()._get_characteristics(character, self.characteristics)

    def set_race(self, character):
        character.chr_race = self._get_race()
        self._get_characteristics(character, self.characteristics)


# Set the race according to the user input
class RaceSetter:
    def __init__(self, race_name):
        # initiate the setter
        self.race_name = race_name
        self.character = Character()
        self.character_race = self.__get_race()

    # get the race according to the user input
    def __get_race(self):
        if self.race_name.upper() == 'AARAKOCRA':
            return Aarakocra(self.race_name)
        elif self.race_name.upper() == 'AVEN':
            return Aven(self.race_name)
        elif self.race_name.upper() == 'BUGBEAR':
            return Aven(self.race_name)
        elif self.race_name.upper() == 'DWARF':
            return Aven(self.race_name)
        elif self.race_name.upper() == 'GOLIATH':
            return Aven(self.race_name)
        else:
            print('You introduced a non-valid character race. Please, select a valid character race')
            return

    # commit all modifications that come with the race
    def set_race(self):
        self.character_race.set_race(self.character)
