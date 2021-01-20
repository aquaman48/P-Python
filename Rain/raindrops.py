"""This file will be for the rain drops we see on the screen in main file"""
import pygame
from pygame.sprite import Sprite

class Rain(Sprite):
	"""Class will represent a rain drop"""
	def __init__(self, rd_game):
		"""Initilize the rain drop and sets starting position"""
		super().__init__()
		self.screen = rd_game.screen

		#image for the rain drop
		self.image = pygame.image.load('images/rain.bmp')
		self.rect = self.image.get_rect()


