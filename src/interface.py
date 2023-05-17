from const import *

class Window:
    def __init__(self) -> None:
        self.x_velocity = 0
        self.y_velocity = 0
        self.x_acceleration = 2
        self.y_acceleration = 0.60
        self.background_width = BACKGROUND[0].get_rect().width

    
    def render_menu_title(self) -> None:
        "renders main menu title"
        
        # renders the title sprite onto the window
        WINDOW.blit(TITLE[0], (195, self.y_velocity+15))
        self.y_velocity += self.y_acceleration

        # If the y position is past a certain range it reverses the change in pixel displacement, so the image moves up or down
        if self.y_velocity > 15:
            self.y_acceleration = -0.60
        
        elif self.y_velocity < -15:
            self.y_acceleration = 0.60


    def render_home_window(self) -> None:
        "renders pygame window and blits sprites onto window"

        # Animation for the home menu background
        scroll_velocity = self.x_velocity % self.background_width
        WINDOW.blit(BACKGROUND[0], (scroll_velocity - self.background_width, 0))

        # If image passes this pixel count, new image is stiched to the end
        if scroll_velocity < 1767:  
            WINDOW.blit(BACKGROUND[0], (scroll_velocity, 0))
         
        self.x_velocity -= self.x_acceleration

        self.render_menu_title()
