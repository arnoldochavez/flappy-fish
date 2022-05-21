__author__ = "arnoldochavez"

import pygame

pygame.font.init()
pygame.mixer.init()

IMAGE = {
	"FISH" : pygame.image.load("assets/images/fish.png"),
	"CORAL" : pygame.image.load("assets/images/coral.png"),
	"SAND_BACK" : pygame.image.load("assets/images/sand-back.png"),
	"SAND_MID" : pygame.image.load("assets/images/sand-mid.png"),
	"SAND_FRONT" : pygame.image.load("assets/images/sand-front.png")
}

FONT = {
	"MAIN" : pygame.font.Font("assets/fonts/Minercraftory.ttf", 18),
	"SCORE" : pygame.font.Font("assets/fonts/Minercraftory.ttf", 24)
}

SOUND = {
	"JUMP" : pygame.mixer.Sound("assets/audio/jump.ogg"),
	"SCORED": pygame.mixer.Sound("assets/audio/scored.ogg"),
	"HIT": pygame.mixer.Sound("assets/audio/hit.ogg")
}