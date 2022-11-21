# Improvised system datatabase
class Database:
    def __init__(self):
        self._users = {'MrCrowley': 'crowley21'}  # the actual "database"

    # check if username present in the database
    def check_user(self, user):
        if user in self._users:
            return True
        else:
            return False

    # verify if the password corresponds to the introduced username
    def verify_user_password(self, user, password):
        if self._users[user] == password:
            return True
        else:
            return False
