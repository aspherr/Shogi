import pygame
import os

pygame.init()

""" WINDOW """
WIDTH, HEIGHT = 900, 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
FPS = 60


""" COLOURS """
WHITE = (220, 220, 220)


""" AUDIO """
UI_SFX = pygame.mixer.Sound(os.path.join('assets', 'sfx', '002-navigation.wav'))
UI_CLICK_SFX = pygame.mixer.Sound(os.path.join('assets', 'sfx', '002-navigation-click.wav'))


""" SPRITES """

BG_SPRITES = [
    "001-home-bg",
    "002-default-bg"
]
BACKGROUND = [pygame.image.load(
                os.path.join('assets', 'sprites', 'menu', 'home', f'{img}.png')) 
                for img in BG_SPRITES]


TITLE_SPRITES = [
    "003-main-title",
    "005-options-title",
    "006-credits-title"
]
TITLE = [pygame.image.load(
                os.path.join('assets', 'sprites', 'menu', 'home', f'{img}.png')) 
                for img in TITLE_SPRITES]


BUTTON_SPRITES = [
    "001-01-start",
    "001-02-start",
    "002-01-manual",
    "002-02-manual",
    "003-01-options",
    "003-02-options",
    "004-01-exit",
    "004-02-exit",
    "005-01-credits",
    "005-02-credits",
    "006-01-engine",
    "006-02-engine",
    "007-01-player",
    "007-02-player",
    "008-01-sente",
    "008-02-sente",
    "009-01-gote",
    "009-02-gote"
]
BUTTON = [pygame.image.load(
                os.path.join('assets', 'sprites', 'menu', 'buttons', f'{img}.png')) 
                for img in BUTTON_SPRITES]


POINTER_SPRITES = [
    "001-menu-pointer",
    "002-01-fwd-pointer",
    "002-02-fwd-pointer",
    "003-01-prev-pointer",
    "003-02-prev-pointer",
    "004-01-mini-fwd-pointer",
    "004-02-mini-fwd-pointer",
    "005-01-mini-prev-pointer",
    "005-02-mini-prev-pointer"
]
POINTER = [pygame.image.load(
                os.path.join('assets', 'sprites', 'menu', 'pointers', f'{img}.png')) 
                for img in POINTER_SPRITES]


""" FONTS """

FONT_1 = pygame.font.SysFont('Savior', 80)
FONT_2 = pygame.font.SysFont('Savior', 50)