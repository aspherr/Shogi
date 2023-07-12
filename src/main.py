"""
Author: Huzaifa Syed
"""

import pygame
import os

from const import *
from interface import *

os.environ["SDL_VIDEO_CENTERD"] = '1'
pygame.init()
pygame.display.set_caption("SHOGI")

class Main:
    def __init__(self) -> None:
        self.menu = Menu()
        self.music = Music()

    def main(self) -> None:
        "Main function"

        self.music.set_sfx_volume(sfx_enabled=True)
        if self.music.is_playing is False:
            self.music.play_track(is_muted=False)
    
        self.menu.window()

        
if __name__ == "__main__":
    app = Main()
    app.main()
