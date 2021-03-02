from pyVariables import *
from buttons import Button
import pygame




class Menu:
    def __init__(self):
        pass


    def create_play_button(self, function=None):
        self.play_button = Button((0,0,90,45),
            function, hover_color=PURPLE2, text="Play")


    def create_pause_button(self, function=None):
        self.pause_button = Button((90,0,90,45),
            function, hover_color=PURPLE2, text="Pause")


    def create_reset_button(self, function=None):
        self.reset_button = Button((180,0,90,45),
            function, hover_color=PURPLE2, text="Clear")


    def create_exploder_sm_button(self, function=None):
        self.exploder_sm_button = Button((360,0,90,45),
            function, hover_color=PURPLE2, text="ExpSmall")


    def create_exploder_button(self, function=None):
        self.exploder_button = Button((450,0,90,45),
            function, hover_color=PURPLE2, text="Exploder")


    def create_toad_button(self, function=None):
        self.toad_button = Button((540,0,90,45),
            function, hover_color=PURPLE2, text="Toad")


    def create_row_button(self, function=None):
        self.row_button = Button((630,0,90,45),
            function, hover_color=PURPLE2, text="Row")


    def create_random_button(self, function=None):
        self.random_button = Button((720,0,90,45),
            function, hover_color=PURPLE2, text="Random")



    def get_event(self, event):
        self.play_button.get_event(event)
        self.pause_button.get_event(event)
        self.reset_button.get_event(event)
        self.exploder_sm_button.get_event(event)
        self.exploder_button.get_event(event)
        self.toad_button.get_event(event)
        self.row_button.get_event(event)
        self.random_button.get_event(event)



    def update(self, surface):
        self.play_button.update(surface)
        self.pause_button.update(surface)
        self.reset_button.update(surface)
        self.exploder_sm_button.update(surface)
        self.exploder_button.update(surface)
        self.toad_button.update(surface)
        self.row_button.update(surface)
        self.random_button.update(surface)




if __name__ == "__main__":
    pygame.init()
    surface = pygame.display.set_mode((DIS_X,DIS_Y))
    surface.fill((BG_COLOR))
    pygame.display.set_caption("Game of Life")

    M = Menu()
    M.create_play_button()
    M.create_pause_button()
    M.create_reset_button()
    M.create_exploder_sm_button()
    M.create_exploder_button()
    M.create_toad_button()
    M.create_row_button()
    M.create_random_button()



    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            M.get_event(event)

        surface.fill((BG_COLOR))
        M.update(surface)
        pygame.display.update()
