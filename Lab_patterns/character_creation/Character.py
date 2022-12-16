from character_creation.State import *
# Singleton implementation
# Mediator
class Character:
    __instance = None  # variable that shows if the instance of that type already exists

    # method to return instance if one does not exist or the existing one in case it was created
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            # set the instance as not initialized
            cls.__instance.__initialized = False
        return cls.__instance

    # initialize the class of type Character
    def __init__(self):
        # return if initialized instance
        if self.__initialized:
            return
        self.__initialized = True
        self.name = None
        self.chr_class = None
        self.chr_race = None
        self.background = None
        self.money_amount = None
        self.saving_throws = None
        self.moral_axis = None
        self.armor = []
        self.normal_state = NormalState(self)
        self.super_state = SuperState(self)
        self.state = self.normal_state
        self.attacks_and_spells = {}
        self.personality_characteristics = {}
        self.appearance = {}
        self.characteristics = {
            'Strength': [0, 0],
            'Dexterity': [0, 0],
            'Constitution': [0, 0],
            'Intelligence': [0, 0],
            'Wisdom': [0, 0],
            'Charisma': [0, 0],
        }

    def switch_to_state(self):
        self.state.switch_to_state()

    def check_special(self):
        self.state.check_special()
