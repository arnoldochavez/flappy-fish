__author__ = "arnoldochavez"

from array import array
import random
import pygame
from . import constants as const
from . import resources as res

pygame.init()

#Keyboard functions
keysList = pygame.key.get_pressed()

def keyboardCheck( key ):
	keys = pygame.key.get_pressed()
	if keys[key]:
		return True
	return False

def keyboardCheckPressed( key ):
	global keysList
	pressed = False
	keys = pygame.key.get_pressed()
	if keys[key] and keysList[key]!=True:
		pressed = True
	keysList = pygame.key.get_pressed()
	return pressed

def playSound( sound ):
	sound = res.SOUND[sound]
	if type(sound) is list:
		sound[random.randint(0, len(sound) - 1)].play()
	else:
		sound.play()