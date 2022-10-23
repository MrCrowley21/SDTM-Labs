# class for database manipulation
class DatabaseManipulator:
    def __init__(self):
        self.cinema_db = {}  # database

    # add a cinematographic object to the database
    def add_to_database(self, cinema):
        title = cinema.get_title()
        if title in self.cinema_db:
            print(f'{title} title already exists')
        else:
            self.cinema_db[cinema.get_id()] = [cinema.get_title(), cinema.player, cinema]

    # check if the id of specified object already in database
    def extract_from_database(self, cinema_id):
        if cinema_id not in self.cinema_db:
            return False
        else:
            return True

    # list database elements with their 'title' field
    def list_db_objects(self):
        for cinema in self.cinema_db:
            print(f'Id: {cinema} - Title: {self.cinema_db[cinema][0]}')
