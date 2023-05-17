import pygame
import os

pygame.init()

""" WINDOW """
WIDTH, HEIGHT = 900, 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
FPS = 60


""" SPRITES """

BG_SPRITES = [
    "001-home-bg",
    "002-default-bg"
]
BACKGROUND = [pygame.image.load(
                os.path.join('assets', 'sprites', 'menu', 'home', f'{img}.png')) 
                for img in BG_SPRITES]


TITLE_SPRITES = [
    "003-main-title"
]
TITLE = [pygame.image.load(
                os.path.join('assets', 'sprites', 'menu', 'home', f'{img}.png')) 
                for img in TITLE_SPRITES]
