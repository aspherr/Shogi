import pygame
import os

from const import *
from interface import *

os.environ["SDL_VIDEO_CENTERD"] = '1'
pygame.init()
pygame.display.set_caption("SHOGI")

class Main:
    def __init__(self) -> None:
        self.window = Window()

    def main(self) -> None:
        "Main function"

        running = True
        while running:
            self.window.render_home_window()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
            pygame.display.update()
            CLOCK.tick(FPS)

        
if __name__ == "__main__":
    app = Main()
    app.main()
