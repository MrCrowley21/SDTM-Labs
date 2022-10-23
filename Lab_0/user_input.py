# class for user definition of new objets
from Lab_0.cinema_operator.cinematographic_object import *


class UserInput:
    def __init__(self, database):
        self.database = database

    # define the movie object using user input and add it to the database
    def user_add_movie(self):
        print('Print the id of the movie:')
        try:
            movie_id = int(input())
        except:
            raise Exception('Id of the movie should be an integer')
        if self.database.extract_from_database(movie_id):
            raise Exception('The specified if already exists')
        print('Print the title of the movie:')
        title = input()
        print("Print the director's name:")
        director_name = input()
        print('Give the duration of the movie:')
        try:
            duration = int(input())
        except:
            raise Exception('Duration should be an integer')
        print('Give the content rating of the movie:')
        try:
            content_rating = int(input())
        except:
            raise Exception('Content rating should be an integer')
        movie = Movie(self.database, movie_id, title, director_name, duration, content_rating)
        self.database.add_to_database(movie)

    # define the serial object using user input and add it to the database
    def user_add_serial(self):
        print('Print the id of the serial:')
        try:
            serial_id = int(input())
        except:
            raise Exception('Id of the movie should be an integer')
        print('Print the title of the serial:')
        title = input()
        print("Print the director's serial:")
        director_name = input()
        print('Give the duration of the serial:')
        try:
            duration = int(input())
        except:
            raise Exception('Duration should be an integer')
        print('Give the content rating of the serial:')
        try:
            content_rating = int(input())
        except:
            raise Exception('Content rating should be an integer')
        print('Give the number of episodes of the serial:')
        try:
            nr_episodes = int(input())
        except:
            raise Exception('Content rating should be an integer')
        serial = Serial(self.database, serial_id, title, director_name, duration, content_rating, nr_episodes)
        self.database.add_to_database(serial)
