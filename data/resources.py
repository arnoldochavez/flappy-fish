__author__ = "arnoldochavez"

import pygame

pygame.font.init()

IMAGE = {
	"FISH" : pygame.image.load("assets/images/fish.png"),
	"CORAL" : pygame.image.load("assets/images/coral.png"),
	"SAND_BACK" : pygame.image.load("assets/images/sand-back.png"),
	"SAND_MID" : pygame.image.load("assets/images/sand-mid.png"),
	"SAND_FRONT" : pygame.image.load("assets/images/sand-front.png")
}

FONT = {
	"MAIN" : pygame.font.Font("assets/fonts/AlteHaasGroteskBold.ttf", 24)
}