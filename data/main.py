__author__ = "arnoldochavez"

from . import control
from .components import player

def main():
	game = control.Control()
	game.main()