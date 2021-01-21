import sys

import pygame



class SpaceMan:
	"""The class for SpaceMan!"""

	def __init__(self):
		"""Initialize the SpaceMan and get him running."""
		pygame.init()

		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		background_image = pygame.image.load('Images/Space.bmp')

		pygame.display.set_caption("Space Man")

	def run_game(self):
		"""Starts the main loop for the game"""
		while True:
			self._check_events()
			self._update_screen()

	def _check_events(self):
		"""Respond to keypresses and mouse events."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	def _update_screen(self):
		"""Update images and flips to new screens"""
		self.background_image.blitme()

		pygame.display.flip()



if __name__ == '__main__':
    # Make a game instance, and run the game.
    sm = SpaceMan()
    sm.run_game()
