__author__ = "arnoldochavez"

import pygame
from .. import constants as const
from .. import tools
from .. import resources as res

class Coral:

	_instances = []

	def __init__( self, x, y ):
		self.x = x
		self.y = y
		self.passed = False
		self.separation = 64
		self.width = 48
		self.height = 256
		self.name = "Coral"
		self.offsetX = 32
		self.offsetY = -56
		self.destroy = False
		self.angleLast = None
		self.angle = 0
		self.depth = 0
		self.side = const.DIR_UP
		self.rect = pygame.Rect(self.x - (self.width/2), self.y + self.separation, self.width, self.height)
		self.control = None
		self.image = res.IMAGE["CORAL"]
		self.imageDraw = None
		self.instanceID = len(type(self)._instances)
		type(self)._instances.append(self)

	def destroyed( self ):
		type(self)._instances.pop(type(self)._instances.index(self))

	def update( self ):
		if self.control.gameState == const.GAMESTATE_RUN:
			self.x -= 2
			if self.x < -self.width:
				self.destroy = True
			if self.side == const.DIR_DOWN:
				self.rect = pygame.Rect(self.x - (self.width/2), self.y + self.separation, self.width, self.height)
			elif self.side == const.DIR_UP:
				self.angle = 180
				self.rect = pygame.Rect(self.x - (self.width/2), self.y - self.height - self.separation, self.width, self.height)
		if self.angleLast != self.angle:
			self.imageDraw = pygame.Surface((self.image.get_width() * 4, self.image.get_height() * 4), pygame.SRCALPHA)
			self.imageDraw.blit(self.image, ((self.imageDraw.get_width()/2) - self.offsetX, (self.imageDraw.get_height()/2) - self.offsetY))
			self.imageDraw = pygame.transform.rotate(self.imageDraw, self.angle)
			self.angleLast = self.angle

	
	def draw( self, surface ):
		if self.imageDraw != None:
			surface.blit(self.imageDraw, (self.x - (self.imageDraw.get_width()/2), self.y - (self.imageDraw.get_height()/2)))
		#DEBUG DRAW
		if const.DEBUG_MODE:
			pygame.draw.rect(surface, (255,0,0), self.rect, 1)
			pygame.draw.line(surface, (0,0,255), (self.x-16, self.y), (self.x+16, self.y),1)
			pygame.draw.line(surface, (0,0,255), (self.x, self.y-16), (self.x, self.y+16),1)
