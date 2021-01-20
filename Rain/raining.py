"""This will be my attempt at doing an exercise that will have rain 
drops streaming down the screen until user presses q to exit out"""


import sys
import pygame

from rain_settings import RainSettings
from raindrops import Rain


class MakeItRain:
	"""The overall class to manage assets and behaviors"""

	def __init__(self):
		"""Initiliaze the program and resources"""
		pygame.init()
		self.rain_settings = RainSettings()

		self.screen = pygame.display.set_mode((self.rain_settings.screen_width, self.rain_settings.screen_height))
		pygame.display.set_caption("Making It Rain")

		self.rainDrops = pygame.sprite.Group()
		self._create_rain()

	def run_game(self):
		"""Start the main loop"""
		while True:
			#watch for keystrokes and mouse events
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
			self.screen.fill(self.rain_settings.bg_color)
			self.rainDrops.draw(self.screen)
			#keeps screen current
			pygame.display.flip()

	def _create_rain(self):
		"""Creates our raindrop"""
		rainDrops = Rain(self)
		self.rainDrops.add(rainDrops)


if __name__ == '__main__':
	"""Make the game instance and run it"""
	rd = MakeItRain()
	rd.run_game()

