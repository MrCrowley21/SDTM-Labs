from character_creation.CharacterCreator import *
from character_creation.CharacterCreationProxy import *

# initialize the proxy of the Character Creation Service
character_creator_proxy = CharacterCreationProxy()

# Check if valid user
if character_creator_proxy.login_user():
    # initialize the class creator
    character_creator = CharacterCreator()
    # create the character
    character_creator.create_character()
    # display all the characteristics of the character
    character_creator.show_character()
# Deny users that are not in database
else:
    print('You must be a valid user to create a character')
