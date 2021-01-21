import pygame

class Settings:
	"""Class that will store the settings for space man"""

	def __init__(self):
		"""initialize the game"""
		self.screen_width = 1200
		self.screen_height = 800
		#loads the space image as the background of the game.
		self.bg_image = pygame.image.load('images/Space.bmp')