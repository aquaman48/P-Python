class GameStats:
	"""Tracks the stats for Alien Invasion"""

	def __init__(self, ai_game):
		"""Initialize statistics"""
		self.settings = ai_game.settings
		self.reset_stats()
		#Start alien invasion in an active state
		self.game_active = True

	def reset_stats(self):
		"""Initialize stats that will change during game"""
		self.ships_left = self.settings.ship_limit
