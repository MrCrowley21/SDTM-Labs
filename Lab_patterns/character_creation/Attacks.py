from abc import ABC, abstractmethod


# Composite Method
class Attack:
    def __init__(self, name):
        self.name = name.upper()

    def get_attack(self):
        if self.name == 'GREATAXE':
            return Greataxe()
        elif self.name == 'HANDAXE':
            return Handaxe()
        elif self.name == 'JAVELIN':
            return Javelin()


class Weapon(ABC):
    @abstractmethod
    def __init__(self, name, weight, damage):
        self.name = name
        self.weight = weight
        self.damage = damage

    @abstractmethod
    def get_characteristics(self):
        pass


# The Leaf Element
class Greataxe(Weapon):
    def __init__(self):
        super().__init__(name='Greataxe', weight=7, damage='1k12')

    def get_characteristics(self):
        return {self.name: {'weight': self.weight, 'damage': self.damage}}


# The Leaf Element
class Handaxe(Weapon):
    def __init__(self):
        super().__init__(name='Handaxe', weight=2, damage='1k6')

    def get_characteristics(self):
        return {self.name: {'weight': self.weight, 'damage': self.damage}}


# The Leaf Element
class Javelin(Weapon):
    def __init__(self):
        super().__init__(name='Javelin', weight=2, damage='1k6')

    def get_characteristics(self):
        return {self.name: {'weight': self.weight, 'damage': self.damage}}


# The composite element
class CharacterAttacks:
    def __init__(self):
        self.attacks = []

    def __create_attack_class(self, weapon):
        concrete_weapon = Attack(weapon).get_attack()
        return concrete_weapon.get_characteristics()

    def add_attack(self, attack):
        attack_class = self.__create_attack_class(attack)
        self.attacks.append(attack_class)

    def remove_attack(self, attack):
        self.attacks.remove(attack)

    def get_attacks(self):
        return self.attacks

