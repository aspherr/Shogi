from const import *

class Window:
    def __init__(self) -> None:
        self.x_velocity = 0
        self.y_velocity = 0
        self.x_acceleration = 2
        self.y_acceleration = 2
        self.background_width = BACKGROUND[0].get_rect().width

    def render_home_window(self) -> None:
        "renders pygame window and blits sprites onto window"

        # Animation for the home menu background
        scroll_velocity = self.x_velocity % self.background_width
        WINDOW.blit(BACKGROUND[0], (scroll_velocity - self.background_width, 0))
        # If image passes this pixel count, new image is stiched to the end
        if scroll_velocity < 1767:  
            WINDOW.blit(BACKGROUND[0], (scroll_velocity, 0))
         
        self.x_velocity -= self.x_acceleration
    