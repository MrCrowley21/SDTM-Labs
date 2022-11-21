# Decorator Method
class CharacterAppearance:
    def __init__(self, character):
        self.character = character

    def render(self):
        return self.character


class Age:
    def __init__(self, wrapped):
        self._wrapped = wrapped
        self.__age = ''

    def __get_age(self):
        print('Please, enter the age of your character')
        self.__age = input()
        return self.__age

    def render(self):
        character = self._wrapped.render()
        character.appearance['age'] = self.__get_age()
        return character


class Height:
    def __init__(self, wrapped):
        self._wrapped = wrapped
        self.__height = ''

    def __get_height(self):
        print('Please, enter the height of your character')
        self.__height = input()
        return self.__height

    def render(self):
        character = self._wrapped.render()
        character.appearance['height'] = self.__get_height()
        return character


class Weight:
    def __init__(self, wrapped):
        self._wrapped = wrapped
        self.__weight = ''

    def __get_weight(self):
        print('It may be uncomfortable but please, enter the weight of your character')
        self.__weight = input()
        return self.__weight

    def render(self):
        character = self._wrapped.render()
        character.appearance['weight'] = self.__get_weight()
        return character


class Eyes:
    def __init__(self, wrapped):
        self._wrapped = wrapped
        self.__eyes = ''

    def __get_eyes_color(self):
        print('What eye color does your character have?')
        self.__eyes = input()
        return self.__eyes

    def render(self):
        character = self._wrapped.render()
        character.appearance['eyes'] = self.__get_eyes_color()
        return character


class Skin:
    def __init__(self, wrapped):
        self._wrapped = wrapped
        self.__skin = ''

    def __get_skin(self):
        print('What skin color does the character have?')
        self.__skin = input()
        return self.__skin

    def render(self):
        character = self._wrapped.render()
        character.appearance['skin'] = self.__get_skin()
        return character


class Hair:
    def __init__(self, wrapped):
        self._wrapped = wrapped
        self.__hair = ''

    def __get_hair(self):
        print('And the last, but not the least, what color does the hair of your character have?')
        self.__hair = input()
        return self.__hair

    def render(self):
        character = self._wrapped.render()
        character.appearance['hair'] = self.__get_hair()
        return character
