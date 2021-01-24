def greet_user(username):
	"""Display a simple greeting."""
	print("Hello, " + username.title() + "!")

greet_user('nick')

def display_message():
	"""Display a simple message"""
	print("Here is a simple function displaying a message.")

display_message()

def pokeFunction():
	"""Having fun"""
	print("Pikachu, I Choose You!")

pokeFunction()

def pokemon(choice):
	"""Choice is the parameter for function pokemon"""
	print("The best pokemon in the world has to be " + choice.title() + "!")
"""Here mewtwo is the argument """
pokemon('mewtwo')

def catch(pokemon1, pType):
	"""Display pokemon info"""
	print("\nI caught a " + pokemon1 + "!")
	print("The " + pokemon1 + " is a " + pType + " type!")
catch('Pikachu', 'Electric')
		