from const import *

class Menu:
    def __init__(self) -> None:
        self.pregame = Pregame()
        
        self.x_velocity = 0
        self.y_velocity = 0
        self.x_acceleration = 2
        self.y_acceleration = 0.60
        self.background_width = BACKGROUND[0].get_rect().width

        self.buttons = [
            Button(BUTTON[0], BUTTON[1], (290, 65), (300, 236), (295, 220), 37, 'large'),
            Button(BUTTON[2], BUTTON[3], (290, 65), (300, 347), (295, 330), 37, 'large'),
            Button(BUTTON[4], BUTTON[5], (290, 65), (300, 457), (295, 440), 37, 'large'),
            Button(BUTTON[6], BUTTON[7], (215, 65), (338, 567), (294, 550), 37, 'large'),
            Button(BUTTON[8], BUTTON[9], (130, 40), (740, 622), (715, 612), 35, 'small')
        ]

            
    def render_title(self) -> None:
        """ renders main menu title """
        
        # renders the title sprite onto the window
        WINDOW.blit(TITLE[0], (195, self.y_velocity+15))
        self.y_velocity += self.y_acceleration

        # title animation
        if self.y_velocity > 15:
            self.y_acceleration = -0.60
        
        elif self.y_velocity < -15:
            self.y_acceleration = 0.60

    
    def window(self) -> None:
        """ renders pygame window and blits sprites onto window """

        # Animation for the home menu background
        scroll_velocity = self.x_velocity % self.background_width
        WINDOW.blit(BACKGROUND[0], (scroll_velocity - self.background_width, 0))

        # If image passes this pixel count, new image is stiched to the end
        if scroll_velocity < 1767:  
            WINDOW.blit(BACKGROUND[0], (scroll_velocity, 0))
         
        self.x_velocity -= self.x_acceleration

        self.render_title()

        for button in self.buttons:
            button.render()
        
        Music().set_sfx_volume(True)
    

    def input(self, event):
        
        self.buttons[0].input()
        if event.type == pygame.MOUSEBUTTONDOWN and self.buttons[0].clicked:
            UI_CLICK_SFX.play()
            self.pregame.opponent_window()
        
        self.buttons[1].input()
        if event.type == pygame.MOUSEBUTTONDOWN and self.buttons[1].clicked:
            UI_CLICK_SFX.play()

        self.buttons[2].input()
        if event.type == pygame.MOUSEBUTTONDOWN and self.buttons[2].clicked:
            UI_CLICK_SFX.play()

        self.buttons[3].input()
        if event.type == pygame.MOUSEBUTTONDOWN and self.buttons[3].clicked:
            UI_CLICK_SFX.play()
            quit()
        
        self.buttons[4].input()
        if event.type == pygame.MOUSEBUTTONDOWN and self.buttons[4].clicked:
            UI_CLICK_SFX.play()


class Pregame:

    def __init__(self) -> None:
        self.buttons = [
            Button(BUTTON[10], BUTTON[11], (290, 82), (300, 275), (295, 220), 37, 'large'),
            Button(BUTTON[12], BUTTON[13], (290, 82), (300, 405), (295, 350), 37, 'large'),
            Button(BUTTON[14], BUTTON[15], (290, 82), (300, 275), (295, 220), 37, 'large'),
            Button(BUTTON[16], BUTTON[17], (290, 82), (300, 405), (295, 350), 37, 'large')
        ]

        self.opponent = ''
        self.colour = ''
    
    
    def opponent_window(self) -> None:

        running = True
        while running:
            WINDOW.blit(BACKGROUND[1], (0, 0))

            for i in range(2):
                self.buttons[i].render()
            
            Music().set_sfx_volume(True)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False
                    exit()
                
                self.opponent_window_input(event)

            pygame.display.update()
            CLOCK.tick(FPS)
    

    def colour_window(self) -> None:

        running = True
        while running:
            WINDOW.blit(BACKGROUND[1], (0, 0))

            for i in range(2):
                self.buttons[i+2].render()

            Music().set_sfx_volume(True)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False
                    exit()
                
                self.colour_window_input(event)

            pygame.display.update()
            CLOCK.tick(FPS)


    def opponent_window_input(self, event) -> None:
        
        self.buttons[0].input()
        if event.type == pygame.MOUSEBUTTONDOWN and self.buttons[0].clicked:
            UI_CLICK_SFX.play()
            self.opponent = 'engine'
            self.colour_window()
            

        self.buttons[1].input()
        if event.type == pygame.MOUSEBUTTONDOWN and self.buttons[1].clicked:
            UI_CLICK_SFX.play()
            self.opponent = 'player'
            self.colour_window()
        
    
    def colour_window_input(self, event) -> None:

        self.buttons[2].input()
        if event.type == pygame.MOUSEBUTTONDOWN and self.buttons[2].clicked:
            UI_CLICK_SFX.play()
            self.colour = 'sente'

        self.buttons[3].input()
        if event.type == pygame.MOUSEBUTTONDOWN and self.buttons[3].clicked:
            UI_CLICK_SFX.play()
            self.colour = 'gote'
        

class Button:

    def __init__(self, unselected_img, selected_img, dimensions, rect_pos, 
                 img_pos, img_center, pointer_size) -> None:
        
        self.button = pygame.Rect(rect_pos, dimensions)
        self.image = unselected_img
        self.selected = selected_img
        self.reset = unselected_img
        self.img_pos = img_pos

        self.pointer_x = rect_pos[0]-80
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
