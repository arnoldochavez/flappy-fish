__author__ = "arnoldochavez"

import pygame
from .. import constants as const
from .. import tools
from .. import resources as res

class SandMiddle:

	_instances = []

	def __init__( self, x, y ):
		self.x = x
		self.y = y
		self.width = 256
		self.height = 46
		self.name = "Sand Middle"
		self.offsetX = 0
		self.offsetY = 46
		self.destroy = False
		self.angle = 0
		self.depth = -1
		self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
		self.control = None
		self.image = res.IMAGE["SAND_MID"]
		self.instanceID = len(type(self)._instances)
		type(self)._instances.append(self)

	def destroyed( self ):
		type(self)._instances.pop(type(self)._instances.index(self))

	def update( self ):
		if self.control.gameState == const.GAMESTATE_RUN or self.control.gameState == const.GAMESTATE_START:
			self.x -= 2
			if self.x < -self.width:
				self.x += len(type(self)._instances) * 256
		self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
	
	def draw( self, surface ):
		#tempSurf = pygame.Surface((self.image.get_width() * 4, self.image.get_height() * 4), pygame.SRCALPHA)
		#tempSurf.blit(self.image, ((tempSurf.get_width()/2) - self.offsetX, (tempSurf.get_height()/2) - self.offsetY))
		#tempSurf = pygame.transform.rotate(tempSurf, self.angle)
		surface.blit(self.image, (self.x - self.offsetX, self.y  - self.offsetY))
		#DEBUG DRAW
		if const.DEBUG_MODE:
			pygame.draw.rect(surface, (255,0,0), self.rect, 1)
			pygame.draw.line(surface, (0,0,255), (self.x-16, self.y), (self.x+16, self.y),1)
			pygame.draw.line(surface, (0,0,255), (self.x, self.y-16), (self.x, self.y+16),1)


class SandBack:

	_instances = []

	def __init__( self, x, y ):
		self.x = x
		self.y = y
		self.width = 256
		self.height = 65
		self.name = "Sand Back"
		self.offsetX = 0
		self.offsetY = 65
		self.destroy = False
		self.angle = 0
		self.depth = -2
		self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
		self.control = None
		self.image = res.IMAGE["SAND_BACK"]
		self.instanceID = len(type(self)._instances)
		type(self)._instances.append(self)

	def destroyed( self ):
		type(self)._instances.pop(type(self)._instances.index(self))

	def update( self ):
		if self.control.gameState == const.GAMESTATE_RUN or self.control.gameState == const.GAMESTATE_START:
			self.x -= 1
			if self.x < -self.width:
				self.x += len(type(self)._instances) * 256
		self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
	
	def draw( self, surface ):
		#tempSurf = pygame.Surface((self.image.get_width() * 4, self.image.get_height() * 4), pygame.SRCALPHA)
		#tempSurf.blit(self.image, ((tempSurf.get_width()/2) - self.offsetX, (tempSurf.get_height()/2) - self.offsetY))
		#tempSurf = pygame.transform.rotate(tempSurf, self.angle)
		surface.blit(self.image, (self.x - self.offsetX, self.y  - self.offsetY))
		#DEBUG DRAW
		if const.DEBUG_MODE:
			pygame.draw.rect(surface, (255,0,0), self.rect, 1)
			pygame.draw.line(surface, (0,0,255), (self.x-16, self.y), (self.x+16, self.y),1)
			pygame.draw.line(surface, (0,0,255), (self.x, self.y-16), (self.x, self.y+16),1)

class SandFront:

	_instances = []

	def __init__( self, x, y ):
		self.x = x
		self.y = y
		self.width = 256
		self.height = 24
		self.name = "Sand Back"
		self.offsetX = 0
		self.offsetY = 24
		self.destroy = False
		self.angle = 0
		self.depth = 2
		self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
		self.control = None
		self.image = res.IMAGE["SAND_FRONT"]
		self.instanceID = len(type(self)._instances)
		type(self)._instances.append(self)

	def destroyed( self ):
		type(self)._instances.pop(type(self)._instances.index(self))

	def update( self ):
		if self.control.gameState == const.GAMESTATE_RUN or self.control.gameState == const.GAMESTATE_START:
			self.x -= 2.5
			if self.x < -self.width:
				self.x += len(type(self)._instances) * 256
		self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
	
	def draw( self, surface ):
		#tempSurf = pygame.Surface((self.image.get_width() * 4, self.image.get_height() * 4), pygame.SRCALPHA)
		#tempSurf.blit(self.image, ((tempSurf.get_width()/2) - self.offsetX, (tempSurf.get_height()/2) - self.offsetY))
		#tempSurf = pygame.transform.rotate(tempSurf, self.angle)
		surface.blit(self.image, (self.x - self.offsetX, self.y  - self.offsetY))
		#DEBUG DRAW
		if const.DEBUG_MODE:
			pygame.draw.rect(surface, (255,0,0), self.rect, 1)
			pygame.draw.line(surface, (0,0,255), (self.x-16, self.y), (self.x+16, self.y),1)
			pygame.draw.line(surface, (0,0,255), (self.x, self.y-16), (self.x, self.y+16),1)
