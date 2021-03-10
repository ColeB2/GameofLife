from pyVariables import *
from board import Board
from menu import Menu
import pygame



class MainState:
    def __init__(self):
        self.B = Board(width=BOARD_WIDTH, height=BOARD_HEIGHT)

        self.run = True
        self.run_game = False

        self.last_cell_change = None

        self.M = Menu()
        self.initialize_buttons_parameters()
        self.create_buttons()
        self.last_update = 0
        self.delay = 500



    """Button Related Methods"""
    def initialize_buttons_parameters(self):
        self.button_info = [
            {"rect":(0,0,90,45),
              "text":"Play",
              "function": self.play_button_function,
              "function_args": None},
            {"rect":(90,0,90,45),
              "text":"Pause",
              "function": self.pause_button_function,
              "function_args": None},
            {"rect":(180,0,90,45),
              "text":"Clear",
              "function": self.B.dead_state,
              "function_args": None},
            {"rect":(550,0,90,45),
              "text":"Exploder",
              "function": self.B.load_state,
              "function_args": "exploder.txt"},
            {"rect":(640,0,90,45),
              "text":"SmallExp.",
              "function": self.B.load_state,
              "function_args": "explodersmall.txt"},
            {"rect":(730,0,90,45),
              "text":"Toad",
              "function": self.B.load_state,
              "function_args": "toad.txt"},
            {"rect":(820,0,90,45),
              "text":"Row",
              "function": self.B.load_state,
              "function_args": "row10cell.txt"},
            {"rect":(910,0,90,45),
              "text":"Random",
              "function": self.B.random_state,
              "function_args": None},
             {"rect": (730,655,90,45),
              "text": "0",
              "function": self.set_delay,
              "function_args": 0},
             {"rect": (820,655,90,45),
              "text": "250",
              "function": self.set_delay,
              "function_args":250 },
             {"rect": (910,655,90,45),
              "text": "500",
              "function": self.set_delay,
              "function_args":500}
        ]


    def create_buttons(self):
        for button in self.button_info:
            self.M.create_buttons(
                                  button["rect"],
                                  button["text"],
                                  button["function"],
                                  button["function_args"])



    def play_button_function(self, *args):
        self.run_game = True


    def pause_button_function(self, *args):
        self.run_game = False


    def set_delay(self, *args):
        self.delay = args[0]


    """Mouse Control Related Methods"""
    def get_cell(self, pos):
        """Converts a mouse position x,y value into a Cell coordinate value and
        returns that value."""
        return (pos[0] - TOP_LEFT_X) // CELL_WIDTH,\
               (pos[1] - TOP_LEFT_Y) // CELL_WIDTH


    def boundary_check(self, i,j):
        """Out of bound check, to test whether the mouse value is outside of the
        board."""
        if i >=0 and i <= BOARD_WIDTH-1  and j >=0 and j <=BOARD_HEIGHT-1:
            return True
        return False


    def click_change(self, pos):
        """Mouse control option:
        Controls state of cell by first finding the i,j value of the cell. Then
        calling the draw_state method on said cell if called. """
        i, j = self.get_cell(pos)
        if self.boundary_check(i,j):
            self.B.board[j][i].draw_state()


    def motion_change(self, pos):
        """Mouse control click and drag control option.
        Controls state of cell via i,j value  and calls the draw state method
        of all cells that come in contact with mouse pointer while click held
        down"""
        i, j = self.get_cell(pos)
        if self.boundary_check(i,j) == True and self.last_cell_change != self.B.board[j][i]:
            self.B.board[j][i].draw_state()
            self.last_cell_change = self.B.board[j][i]


    def mouse_controls(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                self.click_change(pygame.mouse.get_pos())
        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]:
                self.motion_change(pygame.mouse.get_pos())


    def update_state(self, current_time):
        """
        The main board update timing method. Calls the board objects update
        method after self.delay time amount lapses.
        """
        if current_time - self.last_update > self.delay:
            self.B.next_state()
            self.last_update = current_time


    def event_loop(self):
        """The programs main event loop."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

            if not self.run_game:
                self.mouse_controls(event)
            self.M.get_event(event)


    def update(self, surface):
        """Programs main update method"""
        surface.fill(BG_COLOR)
        self.B.update(surface)
        self.M.update(surface, generations=self.B.generation, delay=self.delay)


    def main_loop(self, surface, current_time):
        """Programs main loop. Calls the event loop and the update method as
        well as other methods needed to make the program run."""
        self.event_loop()
        self.update(surface)
        if self.run_game:
            self.update_state(current_time)






if __name__ == "__main__":
    """Sandbox Testing"""
    pygame.init()
    surface = pygame.display.set_mode((DIS_X, DIS_Y))
    surface.fill((BG_COLOR))
    pygame.display.set_caption("Conway's Game of Life mainstate")
    clock = pygame.time.Clock()

    game = MainState()
    while game.run:
        current_time = pygame.time.get_ticks()
        time_delta = clock.tick(FPS)/1000.0
        surface.fill(BG_COLOR)
        game.main_loop(surface, current_time)
        pygame.display.update()
