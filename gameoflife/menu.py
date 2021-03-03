from pyVariables import *
from buttons import Button
import pygame




class Menu:
    def __init__(self):
        self.buttons = []


    def create_buttons(self, rect, button_text, function, function_args=None):
        button = Button((rect), function, hover_color=PURPLE2, text=button_text)
        self.buttons.append(
            {"button": button,
             "function_args":function_args}
        )




    def get_event(self, event):
        for btn_dict in self.buttons:
            btn_dict["button"].get_event(event, btn_dict["function_args"])



    def update(self, surface):
        for btn_dict in self.buttons:
            btn_dict["button"].update(surface)




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
