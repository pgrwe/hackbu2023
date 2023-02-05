import pygame

class Tile(pygame.sprite.Sprite):
	def __init__(self, pos, size):
		"""
			this inits sprite functions and sets instance variables for the rectangle of the wall
			args: self, int, str
			return: none
		"""
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((size,size))
		# self.image = pygame.image.load(image).convert_alpha
		white = (250,250,250)
		self.image.fill(white)
		self.rect = self.image.get_rect(topleft = pos)