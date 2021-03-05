from pyVariables import *
from buttons import Button
import pygame




class Menu:
    def __init__(self):
        self.buttons = []
        self.menu_font = pygame.font.SysFont(None, 50)
        self.render_static_text()



    def create_buttons(self, rect, button_text, function, function_args=None):
        button = Button((rect), function, hover_color=PURPLE2, text=button_text)
        self.buttons.append(
            {"button": button,
             "function_args":function_args}
        )


    def render_static_text(self):
        self.generations_text = self.menu_font.render("Generations: ", True, BLACK, BG_COLOR)
        self.delay_text = self.menu_font.render('Delay(ms): ', True, BLACK, BG_COLOR)


    def render_generations_text(self):
        self.gen_text = self.menu_font.render(str(self.generations), True, BLACK)


    def render_delay_text(self):
        self.delay_text_value = self.menu_font.render(str(self.delay), True, BLACK)


    def blit_text(self, surface):
        surface.blit(self.generations_text, (0,670))
        surface.blit(self.gen_text, (220,670))
        surface.blit(self.delay_text, (300,670))
        surface.blit(self.delay_text_value,(480,670))


    def get_generations(self, generations):
        self.generations = generations
        self.render_generations_text()


    def get_delay(self, delay):
        self.delay = delay
        self.render_delay_text()



    def get_event(self, event):
        for btn_dict in self.buttons:
            btn_dict["button"].get_event(event, btn_dict["function_args"])


    def update(self, surface, **kwargs):
        for btn_dict in self.buttons:
            btn_dict["button"].update(surface)
        self.get_generations(kwargs["generations"])
        self.get_delay(kwargs["delay"])
        self.blit_text(surface)




if __name__ == "__main__":
    pygame.init()
    surface = pygame.display.set_mode((DIS_X,DIS_Y))
    surface.fill((BG_COLOR))
    pygame.display.set_caption("Game of Life")

    M = Menu()



    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            M.get_event(event)

        surface.fill((BG_COLOR))
        M.update(surface)
        pygame.display.update()
