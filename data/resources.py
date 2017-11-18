__author__ = "arnoldochavez"

import pygame

pygame.font.init()

IMAGE = {
	"FISH" : pygame.image.load("assets/images/fish.png"),
	"CORAL" : pygame.image.load("assets/images/coral.png")
}

FONT = {
	"MAIN" : pygame.font.Font("assets/fonts/AlteHaasGroteskBold.ttf", 24)
}
