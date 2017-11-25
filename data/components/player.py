__author__ = "arnoldochavez"

import pygame
from .. import constants as const
from .. import tools
from .. import resources as res
from . import obstacles as obst

class Player:
	def __init__( self, x, y ):
		self.x = x
		self.y = y
		self.width = 32
		self.height = 32
		self.name = "Player"
		self.offsetX = 34
		self.offsetY = 28
		self.verSpeed = 0
		self.verSpeedMax = 10
		self.angle = 0
		self.depth = 1
		self.destroy = False
		self.rect = pygame.Rect(self.x - (self.width/2), self.y - (self.height/2), self.width, self.height)
		self.image = res.IMAGE["FISH"]
		self.control = None

	def destroyed( self ):
		pass

	def update( self ):
		#GAME START
		if self.control.gameState == const.GAMESTATE_START:
			#MOVEMENT
			self.verSpeed = min(self.verSpeed+const.GRAVITY, self.verSpeedMax)
			if self.y > (const.SCREEN_HEIGHT/2) + 32:
				self.verSpeed = -8
			if tools.keyboardCheckPressed(pygame.K_UP):
				self.control.set_gamestate(const.GAMESTATE_RUN)
				print(obst.Coral._instances)
				self.verSpeed = -8
			#UPDATE
			self.angle = -self.verSpeed * 3
			self.y += self.verSpeed
			self.rect = pygame.Rect(self.x - (self.width/2), self.y - (self.height/2), self.width, self.height)
		#GAME RUNING
		elif self.control.gameState == const.GAMESTATE_RUN:
			#COLLISION
			for inst in obst.Coral._instances:
				if inst != self:
					if self.rect.colliderect(inst.rect):
						self.control.set_gamestate(const.GAMESTATE_LOSS)
			if self.y >= const.SCREEN_HEIGHT - 32:
				self.y = const.SCREEN_HEIGHT - 32
				self.verSpeed = -8
				self.control.set_gamestate(const.GAMESTATE_LOSS)
			#MOVEMENT
			self.verSpeed = min(self.verSpeed+const.GRAVITY, self.verSpeedMax)
			if tools.keyboardCheckPressed(pygame.K_UP):
				self.verSpeed = -8
			#UPDATE
			self.angle = -self.verSpeed * 3
			self.y += self.verSpeed
			self.rect = pygame.Rect(self.x - (self.width/2), self.y - (self.height/2), self.width, self.height)
		#GAME OVER
		elif self.control.gameState == const.GAMESTATE_LOSS:
			#FALL
			if self.y < const.SCREEN_HEIGHT - 32:
				self.verSpeed = min(self.verSpeed+const.GRAVITY, self.verSpeedMax)
				self.y = min(self.y + self.verSpeed, const.SCREEN_HEIGHT - 32)
			else:
				self.y = const.SCREEN_HEIGHT - 32
				self.verSpeed = 0
				if tools.keyboardCheckPressed(pygame.K_UP):
					self.control.restart_game()
			#UPDATE
			if (self.verSpeed<0):				
				self.angle = -self.verSpeed * 3
			else:
				self.angle = max(self.angle - 8, -90)
			self.rect = pygame.Rect(self.x - (self.width/2), self.y - (self.height/2), self.width, self.height)
	
	def draw( self, surface ):
		#DRAW ENTITIE WITH ROTATION
		tempSurf = pygame.Surface((self.image.get_width() * 2, self.image.get_height() * 2), pygame.SRCALPHA)
		tempSurf.blit(self.image, ((tempSurf.get_width()/2) - self.offsetX, (tempSurf.get_height()/2) - self.offsetY))
		tempSurf = pygame.transform.rotate(tempSurf, self.angle)
		surface.blit(tempSurf, (self.x - (tempSurf.get_width()/2), self.y - (tempSurf.get_height()/2)))
		#DEBUG DRAW
		if const.DEBUG_MODE:
			pygame.draw.rect(surface, (255,0,0), self.rect, 1)
			pygame.draw.line(surface, (0,0,255), (self.x-16, self.y), (self.x+16, self.y),1)
			pygame.draw.line(surface, (0,0,255), (self.x, self.y-16), (self.x, self.y+16),1)
