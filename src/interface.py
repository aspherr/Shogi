from const import *

class Window:
    def __init__(self) -> None:
        self.x_velocity = 0
        self.y_velocity = 0
        self.x_acceleration = 2
        self.y_acceleration = 0.60
        self.background_width = BACKGROUND[0].get_rect().width

        self.menu_buttons = [
            Button(BUTTON[0], BUTTON[1], (290, 65), (300, 236), (295, 220), 37, 'large'),
            Button(BUTTON[2], BUTTON[3], (290, 65), (300, 347), (295, 330), 37, 'large'),
            Button(BUTTON[4], BUTTON[5], (290, 65), (300, 457), (295, 440), 37, 'large'),
            Button(BUTTON[6], BUTTON[7], (215, 65), (338, 567), (294, 550), 37, 'large'),
            Button(BUTTON[8], BUTTON[9], (130, 40), (740, 622), (715, 612), 35, 'small')
        ]

    
    def render_menu_title(self) -> None:
        """ renders main menu title """
        
        # renders the title sprite onto the window
        WINDOW.blit(TITLE[0], (195, self.y_velocity+15))
        self.y_velocity += self.y_acceleration

        # title animation
        if self.y_velocity > 15:
            self.y_acceleration = -0.60
        
        elif self.y_velocity < -15:
            self.y_acceleration = 0.60


    def render_home_window(self) -> None:
        """ renders pygame window and blits sprites onto window """

        # Animation for the home menu background
        scroll_velocity = self.x_velocity % self.background_width
        WINDOW.blit(BACKGROUND[0], (scroll_velocity - self.background_width, 0))

        # If image passes this pixel count, new image is stiched to the end
        if scroll_velocity < 1767:  
            WINDOW.blit(BACKGROUND[0], (scroll_velocity, 0))
         
        self.x_velocity -= self.x_acceleration

        self.render_menu_title()

        for button in self.menu_buttons:
            button.render()
        
        Music().set_sfx_volume(True)



class Button:

    def __init__(self, unselected_img, selected_img, dimensions, pos, 
                 img_pos, img_center, pointer_size) -> None:
        
        self.button = pygame.Rect(pos, dimensions)
        self.image = unselected_img
        self.selected = selected_img
        self.reset = unselected_img
        self.img_pos = img_pos

        self.pointer_x = pos[0]-80
        self.pointer_y = self.button.center[1] - (img_center-5)
        self.pointer_size = pointer_size

        self.clicked = False
        self.play_sound = True
    

    def input(self) -> None:
        """ monitors button input """
        
        mouse_pos = pygame.mouse.get_pos()
        if self.button.collidepoint(mouse_pos):  # checks if mouse is on button
            self.image = self.selected
            
            if self.play_sound:
                self.play_sound = False
                UI_SFX.play()

            if self.pointer_size == 'large':
                WINDOW.blit(POINTER[0], (self.pointer_x, self.pointer_y))
            
            else:
                WINDOW.blit(POINTER[1], (self.pointer_x+20, self.pointer_y+4))
            
            # checks for mouse clicks whilst over button
            if pygame.mouse.get_pressed()[0]:
                self.clicked = True
                
            elif self.clicked:
                self.clicked = False
                UI_CLICK_SFX.play()
        
        # unhighlights image
        else:
            self.image = self.reset
            self.clicked = False
            self.play_sound = True
            
    
    def render(self) -> None:
        """ renders button """

        self.input()
        WINDOW.blit(self.image, self.img_pos)


class Music:

    def __init__(self) -> None:
        self.is_playing = pygame.mixer.music.get_busy()
        self.volume = [0.2, 0.2]
        self.sfx = [
            UI_SFX,
            UI_CLICK_SFX
        ]

    def play_track(self):

        pygame.mixer.music.load((os.path.join('assets', 'sfx', '001-bgm.wav')))
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.1)

    

    def set_sfx_volume(self, sfx_enabled):

        if not sfx_enabled:
            for file in self.sfx:
                file.set_volume(0)
        
        else:
            for i, file in enumerate(self.sfx):
                file.set_volume(self.volume[i])
