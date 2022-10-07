# class for user control over the system
from user_input import *
from Lab_1.cinema_operator.rating_system import *


class Control:
    def __init__(self, database):
        self.database = database
        self.rating_system = RatingSystem()

    # select from the list of existing cinematographic objets
    def list_existing_objects(self):
        print('Write the id of the cinematographic object you want to watch')
        self.database.list_db_objects()
        try:
            cinema_id = int(input())
        except:
            raise Exception('Cinema id should be an integer')
        if not self.database.extract_from_database(cinema_id):
            raise Exception('You selected a non-valid id')
        return cinema_id

    # define user's choice
    def user_choose_action(self):
        print('Press the corresponding number of the action you want to perform:\n'
              '1 - Add a movie\n'
              '2 - Add a serial\n'
              '3 - Watch something\n'
              '4 - Rate something')
        # extract and select validity of the input choice
        try:
            action = int(input())
        except:
            raise Exception('To select an action, select the corresponded number')
        if action < 1 or action > 4:
            raise Exception('To select an action, select the corresponded number')
        # add a movie choice
        if action == 1:
            UserInput(self.database).user_add_movie()
        # add a serial choice
        elif action == 2:
            UserInput(self.database).user_add_serial()
        # watch choice
        elif action == 3:
            cinema_id = self.list_existing_objects()
            self.database.cinema_db[cinema_id][1].play()
        # rate choice
        elif action == 4:
            cinema_id = self.list_existing_objects()
            cinema = self.database.cinema_db[cinema_id][2]
            print(f"The current rating is {cinema.rating}")
            self.rating_system.give_rating(cinema)
            self.rating_system.modify_general_rating(cinema)
            print(f"The current rating is {cinema.rating}")
