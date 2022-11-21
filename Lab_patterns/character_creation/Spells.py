from abc import ABC, abstractmethod


# Composite Method
class Spells:
    def __init__(self, name):
        self.name = name.upper()

    def get_spell(self):
        if self.name == 'ACID SPLASH':
            return AcidSplash()
        elif self.name == 'CHILL TOUCH':
            return ChillTouch()
        elif self.name == 'ENCODE THOUGHTS':
            return EncodeThoughts()


class Spell(ABC):
    @abstractmethod
    def __init__(self, name, s_range, duration):
        self.name = name
        self.s_range = s_range
        self.duration = duration

    @abstractmethod
    def get_characteristics(self):
        pass


# The Leaf Element
class AcidSplash(Spell):
    def __init__(self):
        super().__init__(name='Acid Splash', s_range=60, duration='Instantaneous')

    def get_characteristics(self):
        return {self.name: {'s_range': self.s_range, 'duration': self.duration}}


# The Leaf Element
class ChillTouch(Spell):
    def __init__(self):
        super().__init__(name='Chill Touch', s_range=120, duration='1 round')

    def get_characteristics(self):
        return {self.name: {'s_range': self.s_range, 'duration': self.duration}}


# The Leaf Element
class EncodeThoughts(Spell):
    def __init__(self):
        super().__init__(name='Encode Thoughts', s_range='self', duration='8 hours')

    def get_characteristics(self):
        return {self.name: {'s_range': self.s_range, 'duration': self.duration}}


# The composite element
class CharacterSpells:
    def __init__(self):
        self.spells = []

    def __create_spell_class(self, spell):
        concrete_spell = Spells(spell).get_spell()
        return concrete_spell.get_characteristics()

    def add_spell(self, spell):
        spell_class = self.__create_spell_class(spell)
        self.spells.append(spell_class)

    def remove_spell(self, spell):
        self.spells.remove(spell)

    def get_spells(self):
        return self.spells

