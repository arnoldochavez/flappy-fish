__author__ = "arnoldochavez"

import pygame
from .. import constants as const
from .. import tools

class Coral:
	def __init__( self, x, y ):
		self.x = x
		self.y = y
		self.separation = 64
		self.width = 48
		self.height = 256
		self.name = "Coral"
		self.offsetX = 34
		self.offsetY = 28
		self.destroy = False
		self.side = const.DIR_UP
		self.rect = pygame.Rect(self.x - (self.width/2), self.y + self.separation, self.width, self.height)
		self.control = None

	def update( self ):
		if self.control.gameState == const.GAMESTATE_RUN:
			self.x -= 2
			if self.x < -self.width:
				self.destroy = True
			if self.side == const.DIR_DOWN:
				self.rect = pygame.Rect(self.x - (self.width/2), self.y + self.separation, self.width, self.height)
			elif self.side == const.DIR_UP:
				self.rect = pygame.Rect(self.x - (self.width/2), self.y - self.height - self.separation, self.width, self.height)
	
	def draw( self, surface ):
		"""tempSurf = pygame.Surface((self.image.get_width() * 2, self.image.get_height() * 2), pygame.SRCALPHA)
		tempSurf.blit(self.image, ((tempSurf.get_width()/2) - self.offsetX, (tempSurf.get_height()/2) - self.offsetY))
		tempSurf = pygame.transform.rotate(tempSurf, self.angle)
		surface.blit(tempSurf, (self.x - (tempSurf.get_width()/2), self.y - (tempSurf.get_height()/2)))"""
		pygame.draw.rect(surface, (255,0,0), self.rect, 1)
		pygame.draw.line(surface, (0,0,255), (self.x-16, self.y), (self.x+16, self.y),1)
		pygame.draw.line(surface, (0,0,255), (self.x, self.y-16), (self.x, self.y+16),1)
