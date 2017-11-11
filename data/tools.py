__author__ = "arnoldochavez"

import pygame
from . import constants as const

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