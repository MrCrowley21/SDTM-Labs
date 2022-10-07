# classes for describing the cinematographic objects
from cinema_player import *


# define general class (a.k.a. interface) for a cinematographic object
class CinematographicObject:
    def __init__(self, database, cinema_id: int, name: str, director: str, duration_min: int, content_rating: int,
                 nr_episodes: int):
        self.database = database
        self._cinema_id = cinema_id
        self._name = name
        self._director = director
        self._duration_min = duration_min
        self._nr_episodes = nr_episodes
        self._content_rating = content_rating
        self.rating = 0
        self.rating_list = []

    def get_id(self):
        return self._cinema_id

    def get_title(self):
        return self._name

    def get_rating(self):
        return self.rating

    def get_content_rating(self):
        return self._content_rating

    def get_details(self):
        return self.__dict__

    def get_total_duration(self):
        return self._duration_min

    def get_nr_episodes(self):
        return self._nr_episodes


# define movie object
class Movie(CinematographicObject):
    def __init__(self, database, movie_id: int, name: str, director: str, duration_min: int, content_rating: int):
        super().__init__(database, movie_id, name, director, duration_min, content_rating, nr_episodes=1)
        self.rating_list = []
        self.player = MoviePlayer(self, database)

    def get_id(self):
        movie_id = super().get_id()
        return movie_id

    def get_title(self):
        title = super().get_title()
        return title

    def get_rating(self):
        rating = super().get_rating()
        return rating

    def get_content_rating(self):
        content_rating = super().get_content_rating()
        return content_rating

    def get_details(self):
        details = super().get_details()
        return details

    def get_total_duration(self):
        duration_min = super().get_total_duration()
        return duration_min

    def get_nr_episodes(self):
        return 1


# define serial object
class Serial(CinematographicObject):
    def __init__(self, database, series_id: int, name: str, director: str, duration_min: int, content_rating: int,
                 nr_episodes: int):
        super().__init__(database, series_id, name, director, duration_min, content_rating, nr_episodes)
        self.rating_list = []
        self.player = SerialPlayer(self, database)

    def get_id(self):
        serial_id = super().get_id()
        return serial_id

    def get_title(self):
        title = super().get_title()
        return title

    def get_rating(self):
        rating = super().get_rating()
        return rating

    def get_content_rating(self):
        content_rating = super().get_content_rating()
        return content_rating

    def get_details(self):
        details = super().get_details()
        return details

    def get_total_duration(self):
        return self._duration_min * self._nr_episodes

    def get_nr_episodes(self):
        nr_episodes = super().get_nr_episodes()
        return nr_episodes
