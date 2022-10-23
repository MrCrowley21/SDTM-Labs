# classes for describing the cinematographic objects
from time import sleep
import keyboard


# define general class (a.k.a. interface) for a player object
class CinemaPlayer:
    def __init__(self, cinema, database):
        self._database = database
        self._cinema = cinema
        self._content_rating = cinema.get_content_rating()
        self._duration = cinema.get_total_duration()

    # define the abstract start button
    def _start(self, remained_duration):
        while True:
            sleep(1)
            remained_duration -= 1
            print(remained_duration)
            try:
                if keyboard.is_pressed('shift') or remained_duration == 0:
                    return remained_duration
            except:
                pass

    # define abstract pause button
    def _pause(self):
        while True:
            if keyboard.read_key() == 'ctrl':
                break

    # define the player for cinematography object
    def _play(self):
        if self._database.extract_from_database(self._cinema.get_id()):
            print(f'You are watching {self._cinema.get_title()}')
            remained_duration = self._duration
            is_started = 1
            print('Press:\n "Shift" - to pause the player\n "Ctrl" - to start the player')
            while remained_duration > 0:
                if is_started == 1:
                    remained_duration = self._start(remained_duration)
                    is_started = 0
                else:
                    self._pause()
                    is_started = 1
            print(f'You have watched {self._cinema.get_title()}')
        else:
            return f'Cannot play {self._cinema.get_title()} as it is not in database'


# define the movie player
class MoviePlayer(CinemaPlayer):
    def __init__(self, cinema, database):
        super().__init__(cinema, database)

    def start(self, remained_duration):
        print('You have started the movie')
        remained_duration = self._start(remained_duration)
        return remained_duration

    def pause(self):
        print('You have paused the movie')
        super()._pause()

    def play(self):
        if self._database.extract_from_database(self._cinema.get_id()):
            print(f'You are watching {self._cinema.get_title()}')
            remained_duration = self._duration
            is_started = 1
            print('Press:\n "Shift" - to pause the player\n "Ctrl" - to start the player')
            while remained_duration > 0:
                if is_started == 1:
                    remained_duration = self.start(remained_duration)
                    is_started = 0
                else:
                    self.pause()
                    is_started = 1
            print(f'You have watched {self._cinema.get_title()}')
        else:
            return f'Cannot play {self._cinema.get_title()} as it is not in database'


# define the serial player
class SerialPlayer(CinemaPlayer):
    def __init__(self, cinema, database):
        super().__init__(cinema, database)
        self._nr_episodes = cinema.get_nr_episodes()

    def choose_episode(self):
        print(f'Choose an episode from {self._nr_episodes} available')
        try:
            episode = int(input())
        except:
            raise Exception('Episode should be an integer number')
        if episode < 0 or episode > self._nr_episodes:
            raise Exception('Not available episode')
        return episode

    def get_episode_duration(self):
        print(self._duration // self._nr_episodes)
        return self._duration // self._nr_episodes

    def start(self, remained_duration):
        print('You have started the serial')
        print(remained_duration)
        remained_duration = super()._start(remained_duration)
        return remained_duration

    def pause(self):
        print('You have paused the serial')
        super()._pause()

    def play(self):
        self.choose_episode()
        if self._database.extract_from_database(self._cinema.get_id()):
            print(f'You are watching {self._cinema.get_title()}')
            remained_duration = self.get_episode_duration()
            is_started = 1
            print('Press:\n "Shift" - to pause the player\n "Ctrl" - to start the player')
            while remained_duration > 0:
                if is_started == 1:
                    remained_duration = self.start(remained_duration)
                    is_started = 0
                else:
                    self.pause()
                    is_started = 1
            print(f'You have watched {self._cinema.get_title()}')
        else:
            return f'Cannot play {self._cinema.get_title()} as it is not in database'
