from character_creation.CharacterCreationDataBase import *
from character_creation.CharacterCreator import *


# Proxy Method
class CharacterCreationProxy:
    def __init__(self):
        self.db = Database()
        self.character_creator = None

    # check if the introduced username is in database
    def __check_user_existence(self, username):
        if self.db.check_user(username):
            return True
        # ask for another username in case a wrong one was introduces
        else:
            print('Incorrect username. Try again!')
            return False

    # validate the user according to the password he/she introduced
    def __check_password(self, username, password):
        if self.db.verify_user_password(username, password):
            return True
        else:
            print('Incorrect password. Try to login the system again!')
            return False

    # process of user's registration
    def login_user(self):
        print('To use our service you must log in first!')
        print('Introduce your username: ')
        username = input()
        if self.__check_user_existence(username):
            print('Introduce your password:')
            password = input()
            if self.__check_password(username, password):
                return CharacterCreator()
            # Exit the system if the wrong password was introduced
            else:
                return False
        else:
            self.login_user()
