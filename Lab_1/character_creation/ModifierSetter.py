from abc import ABC, abstractmethod
from copy import deepcopy

from character_creation.Character import *


# Prototype Method implementation

# Implementation of abstract prototype method
class AbstractModifierSetter(ABC):
    # abstract method to clone an object (deep coopy in this case)
    @abstractmethod
    def clone(self):
        return deepcopy(self)


# Implementation of concrete ModifierSetter implementation
class ModifierSetter(AbstractModifierSetter):
    # setter initiation
    def __init__(self):
        self.character = Character()
        self.modifiers = {}

    # get the character's modifiers according to his/her general characteristics
    def get_modifier(self):
        for char in self.character.characteristics:
            self.modifiers[char] = -5 + self.character.characteristics[char][0] // 2
        return self.modifiers

    # clone method of the object of ModifierSetter type
    def clone(self):
        copy = super().clone()
        return copy
