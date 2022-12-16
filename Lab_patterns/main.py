from character_creation.CharacterCreator import *
from character_creation.CharacterCreationProxy import *

# initialize the proxy of the Character Creation Service
character_creator_proxy = CharacterCreationProxy()

# Check if valid user
if character_creator_proxy.login_user():
    # create the character
    receiver = Receiver()
    invoker = Invoker()
    command = CharacterCreator(receiver)
    invoker.register("custom_call", command)
    invoker.execute("custom_call")
    # display all the characteristics of the character
    command.show_character()
# Deny users that are not in database
else:
    print('You must be a valid user to create a character')
