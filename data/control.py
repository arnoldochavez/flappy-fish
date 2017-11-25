__author__ = "arnoldochavez"

import random
import pygame
from . import resources as res
from . import constants as const
from .components import player
from .components import obstacles
from .components import backgrounds as back

pygame.init()

class Control( object ):

	def __init__( self ):
		self.gameState = const.GAMESTATE_START
		self.display = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
		self.done = False
		self.clock = pygame.time.Clock()
		self.fps = 60
		self.spawnObstaclesTimer = self.fps * 2
		self.instances = []
		self.blinkScreenAlpha = 0
		self.blinkScreenEnd = False

	def event_loop( self ):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.done = True

	def spawn_obstacles( self ):
		randSeparation = random.randrange(-64,64)
		self.instance_create(const.SCREEN_WIDTH+64, (const.SCREEN_HEIGHT/2) + randSeparation, obstacles.Coral).side = const.DIR_UP
		self.instance_create(const.SCREEN_WIDTH+64, (const.SCREEN_HEIGHT/2) + randSeparation, obstacles.Coral).side = const.DIR_DOWN		

	def start( self ):
		self.gameState = const.GAMESTATE_START
		self.blinkScreenEnd = False
		self.instance_create(const.SCREEN_WIDTH/2, const.SCREEN_HEIGHT/2,player.Player)
		for i in range(0, int(const.SCREEN_WIDTH/256)+2):
			self.instance_create(i*256, const.SCREEN_HEIGHT, back.SandMiddle)
			self.instance_create(i*256, const.SCREEN_HEIGHT, back.SandBack)
			self.instance_create(i*256, const.SCREEN_HEIGHT, back.SandFront)

	def update( self ):
		#UPDATE ALL INSTANCES
		for inst in self.instances:
			inst.update()
		for inst in self.instances:
			if inst.destroy:
				inst.destroyed()
				self.instances.remove(inst)

		#SELF UPDATE STEP
		#SPAWN OBSTACLES
		if self.gameState == const.GAMESTATE_RUN:
			if self.spawnObstaclesTimer > 0:
				self.spawnObstaclesTimer -= 1
			else:
				self.spawnObstaclesTimer = self.fps * 2
				self.spawn_obstacles()
		#END SPAWN OBSTACLES
		elif self.gameState == const.GAMESTATE_LOSS:
			if not self.blinkScreenEnd:
				if self.blinkScreenAlpha<255:
					self.blinkScreenAlpha = min(self.blinkScreenAlpha + 50, 255)
				else:
					self.blinkScreenAlpha = 255
					self.blinkScreenEnd = True
			else:
				if self.blinkScreenAlpha>0:
					self.blinkScreenAlpha = max(self.blinkScreenAlpha - 50, 0)
				else:
					self.blinkScreenAlpha = 0

	def draw( self ):
		#DRAW ALL INSTANCES
		self.display.fill(const.SCREEN_COLOR)
		self.instances.sort(key=lambda x: x.depth)
		for inst in self.instances:
			inst.draw(self.display)
		if self.gameState == const.GAMESTATE_LOSS:
			surf = pygame.Surface((self.display.get_width(),self.display.get_height()), pygame.SRCALPHA)
			surf.fill((255,255,255,self.blinkScreenAlpha))
			self.display.blit(surf,(0,0))
		if self.gameState == const.GAMESTATE_START:
			#self.draw_text("PRESS UP!", const.SCREEN_WIDTH/2, const.SCREEN_HEIGHT - 14, const.ALIGN_CENTER, (255,161,17))
			self.draw_text("PRESS UP!", const.SCREEN_WIDTH/2, const.SCREEN_HEIGHT - 16, const.ALIGN_CENTER, (255,255,255))

	def main( self ):
		self.start()
		while not self.done:
			self.event_loop()
			self.update()
			self.draw()
			pygame.display.flip()
			self.clock.tick(self.fps)

	def set_gamestate( self, state ):
		self.gameState = state

	def restart_game( self ):
		for inst in self.instances:
			inst.destroyed()
		del self.instances[:]
		self.start()

	def draw_text( self, text, x, y, align = const.ALIGN_LEFT, color = (0,0,0), font = res.FONT["MAIN"]):
		surf = font.render(text, True, color)
		if align == const.ALIGN_LEFT:
			self.display.blit(surf, (x, y - surf.get_height()))
		elif align == const.ALIGN_CENTER:
			self.display.blit(surf, (x - (surf.get_width()/2), y - surf.get_height()))
		elif align == const.ALIGN_RIGHT:
			self.display.blit(surf, (x - surf.get_width(), y - surf.get_height()))

	def instance_create( self, x, y, obj ):
		inst = obj(x, y)
		inst.control = self
		self.instances.append(inst)
		return inst