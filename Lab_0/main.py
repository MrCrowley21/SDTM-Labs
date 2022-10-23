from Lab_0.cinema_operator.db_manipulator import *
from control import *

# initiate the used classes
database = DatabaseManipulator()
control = Control(database)

# initiate the communication with the user
while True:
    control.user_choose_action()
