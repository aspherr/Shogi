import pygame
import os

pygame.init()

""" WINDOW """
WIDTH, HEIGHT = 900, 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
FPS = 60


""" DIMENSIONS. """
BOARD_SIZE = (170, 87, 550, 550)
KOMA1_SIZE = (799, 86, 62, 428)
KOMA2_SIZE = (39, 216, 62, 428)

BOARD_TILE_SIZE = BOARD_SIZE[2] // 9
KOMA_TILE_SIZE = KOMA1_SIZE[3] / 7

BOARD_X, BOARD_Y = BOARD_SIZE[0], BOARD_SIZE[1]
KOMA1_X, KOMA1_Y = KOMA1_SIZE[0], KOMA1_SIZE[1]
KOMA2_X, KOMA2_Y = KOMA2_SIZE[0], KOMA2_SIZE[1]


""" COLOURS """
WHITE = (220, 220, 220)
GREEN = (16, 180, 110)
GREY1 = (48, 48, 48)
GREY2 = (75, 75, 75)
RED = (255, 65, 65)


""" AUDIO """
UI_SFX = pygame.mixer.Sound(os.path.join('assets', 'sfx', '002-navigation.wav'))
UI_CLICK_SFX = pygame.mixer.Sound(os.path.join('assets', 'sfx', '002-navigation-click.wav'))
MOVE_SFX = pygame.mixer.Sound(os.path.join('assets', 'sfx', '005-move.wav'))
CAPTURE_SFX = pygame.mixer.Sound(os.path.join('assets', 'sfx', '006-capture.wav'))
CHECK_SFX = pygame.mixer.Sound(os.path.join('assets', 'sfx', '007-check.wav'))


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
    "004-manual-title",
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
    "009-02-gote",
    "010-01-sfx",
    "010-02-sfx",
    "011-01-music",
    "011-02-music"
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


GAME_INFO_SPRITES = [
    '001-game-info',
    '002-game-info',
    '003-game-info',
    '004-game-info',
    '005-game-info'
]
GAME_SLIDES = [pygame.image.load(
                    os.path.join('assets', 'sprites', 'menu', 'guide', 'game info', f'{img}.png')) 
                    for img in GAME_INFO_SPRITES]


BOARD_INFO_SPRITES = [
    '001-board-info',
    '002-board-info',
    '003-board-info',
    '004-board-info',
    '005-board-info',
    "006-board-info"
]
BOARD_SLIDES = [pygame.image.load(
                    os.path.join('assets', 'sprites', 'menu', 'guide', 'board info', f'{img}.png')) 
                    for img in BOARD_INFO_SPRITES]


PIECE_INFO_SPRITES = [
    '001-piece-P',
    '002-piece-L',
    '003-piece-N',
    '004-piece-S',
    '005-piece-G',
    '006-piece-B',
    '007-piece-R',
    '008-piece-K',
    '009-piece-PP',
    '010-piece-PL',
    '011-piece-PN',
    '012-piece-PS',
    '013-piece-PB',
    '014-piece-PR'
]
PIECES_SLIDES = [pygame.image.load(
                    os.path.join('assets', 'sprites', 'menu', 'guide', 'piece info', f'{img}.png')) 
                    for img in PIECE_INFO_SPRITES]


BOARD_SPRITE = pygame.image.load(os.path.join('assets', 'sprites', 'board', '001-board.png'))
KOMA1_SPRITE = pygame.image.load(os.path.join('assets', 'sprites', 'komadai', '003-01-koma.png'))
KOMA2_SPRITE = pygame.image.load(os.path.join('assets', 'sprites', 'komadai', '004-02-koma.png'))


SENTE_PIECES_SPRITES = [
    '001-P1',
    '002-L1',
    '003-N1',
    '004-S1',
    '005-G1',
    '006-B1',
    '007-R1',
    '008-K1'
]
SENTE_PIECES = [pygame.image.load(
                    os.path.join('assets', 'sprites', 'pieces', f'{img}.png')) 
                    for img in SENTE_PIECES_SPRITES]


GOTE_PIECES_SPRITES = [
    '015-P2',
    '016-L2',
    '017-N2',
    '018-S2',
    '019-G2',
    '020-B2',
    '021-R2',
    '022-K2'
]
GOTE_PIECES = [pygame.image.load(
                    os.path.join('assets', 'sprites', 'pieces', f'{img}.png')) 
                    for img in GOTE_PIECES_SPRITES]


""" BOUNDS """
TOP, BOTTOM = 0, 8
LEFT, RIGHT = 0, 8


""" FONTS """

FONT_1 = pygame.font.SysFont('Savior', 80)
FONT_2 = pygame.font.SysFont('Savior', 50)

