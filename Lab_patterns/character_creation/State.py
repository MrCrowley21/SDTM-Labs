# State Pattern
# Base state
class State:
    def check_special(self):
        self.range += 1
        if self.range == len(self.addons):
            self.range = 0
            self.switch_to_state()

    def __repr__(self):
        if self.range != 0:
            return 'On'
        else:
            return 'Off'


# Concrete state
class NormalState(State):
    def __init__(self, character):
        self.character = character
        self.addons = ['1 up', '2 up', '3 up']
        self.range = 1

    def switch_to_state(self):
        self.character.state = self.character.super_state


# Concrete state
class SuperState(State):
    def __init__(self, character):
        self.character = character
        self.addons = ['1 down', '2 down', '3 down']
        self.range = 0

    def switch_to_state(self):
        self.character.state = self.character.normal_state

